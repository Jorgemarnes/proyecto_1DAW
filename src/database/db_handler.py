from types import TracebackType

import psycopg2
from psycopg2.extras import execute_values

from src.settings.settings import HOST, PORT


class DBHandler:
    """Handles the lifecycle and bulk data insertion for the PostgreSQL database."""
    
    def __init__(self, *, username: str, password: str):
        self._config = {
            'dbname': 'Music_Licenses',
            'user': username,
            'password': password,
            'host': HOST,
            'port': PORT
        }
        self.con = None
        self.cur = None

    def __enter__(self):
        self.con = psycopg2.connect(**self._config) # type: ignore[call-overload]
        self.cur = self.con.cursor()
        print('[DB] Connection successfully established.')
        return self

    def __exit__(
        self,
        exc_type: BaseException | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None
    ) -> bool:
        if exc_type:
            print(f'[DB] Exiting due to system error ({exc_val}). Applying rollback...')
            self.con.rollback() # type: ignore[reportOptionalMemberAccess]
        try:
            self.con.commit() # type: ignore[reportOptionalMemberAccess]
            print('[DB] Transaction committed successfully.')
        except Exception as e:
            print(f'[DB] Error committing transaction: {e}')
            self.con.rollback() # type: ignore[reportOptionalMemberAccess]
        self.cur.close() # type: ignore[reportOptionalMemberAccess]
        self.con.close() # type: ignore[reportOptionalMemberAccess]
        print('[DB] Connection and cursor closed')
        return False # Return False to let any unexpected exception propagate normally

    def insert_scraped_data(self, tracks: list) -> None:
        """Processes raw API data and performs insertion handling duplicates."""
        if not tracks:
            print('[DB] No tracking data provided for insertion.')
            return

        artists = albums = songs = belongs = contains = set()

        for track in tracks:
            if not all(k in track for k in ['artistId', 'collectionId', 'trackId']):
                continue
            artists.add((track.get('artistId'), track.get('artistName')))
            albums.add((
                track.get('collectionId'), 
                track.get('artistId'), 
                track.get('collectionName'), 
                track.get('artworkUrl100'), 
                track.get('releaseDate')
            ))
            songs.add((
                track.get('trackId'), 
                track.get('collectionId'), 
                track.get('trackName'), 
                track.get('trackTimeMillis'), 
                track.get('previewUrl')
            ))
            belongs.add((track.get('artistId'), track.get('collectionId')))
            contains.add((track.get('collectionId'), track.get('trackId')))

        try:
            execute_values(self.cur, """
                INSERT INTO artist (id, name) 
                VALUES %s
                ON CONFLICT (id) DO NOTHING;
            """, artists)
            execute_values(self.cur, """
                INSERT INTO album (id, artist_id, title, cover_url, release_date) 
                VALUES %s
                ON CONFLICT (id) DO NOTHING;
            """, albums)
            execute_values(self.cur, """
                INSERT INTO song (id, album_id, title, duration, preview_url) 
                VALUES %s
                ON CONFLICT (id) DO NOTHING;
            """, songs)
            execute_values(self.cur, """
                INSERT INTO artist_album (artist_id, album_id) 
                VALUES %s
                ON CONFLICT (artist_id, album_id) DO NOTHING;
            """, belongs)
            execute_values(self.cur, """
                INSERT INTO album_song (album_id, song_id) 
                VALUES %s
                ON CONFLICT (album_id, song_id) DO NOTHING;
            """, contains)
            print(f'[DB] Bulk load finished. Processed: {len(songs)} songs in {len(albums)} albums.')
        except Exception as e:
            print(f'[DB Error] SQL transaction failed. Rollback applied: {e}')
            raise e   
