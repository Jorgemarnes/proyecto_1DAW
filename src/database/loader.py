import psycopg2
from psycopg2.extras import execute_values
from config.config import DB_CONFIG

class DBHandler:
    """Handles the lifecycle and bulk data insertion for the PostgreSQL database."""
    
    def __init__(self):
        self.config = DB_CONFIG
        self.con = None
        self.cur = None

    def __enter__(self):
        self.con = psycopg2.connect(**self.config)
        self.cur = self.con.cursor()
        print('[DB] Connection successfully established.')
        return self

    def __exit__(self, exc_type, exc_val):
        if exc_type:
            print(f'[DB] Exiting due to system error ({exc_val}). Applying rollback...')
            if self.con:
                self.con.rollback()
        if self.cur:
            self.cur.close()
        if self.con:
            self.con.close()
        print('[DB] Connection and cursor closed automatically.')
        return False # Return False to let any unexpected exception propagate normally

    def insert_scraped_data(self, tracks: list):
        """Processes raw API data and performs bulk insertion."""
        if not tracks:
            print('[DB] No tracking data provided for insertion.')
            return
        for track in tracks:
            artists = albums = belongs = songs = contains = {}
            if not all(k in track for k in ['artistId', 'collectionId', 'trackId']):
                continue
            artists['id'] = track.get('artistId')
            artists['name'] = track.get('artistName')
            albums['id'] = track.get('collectionId')
            albums['artist_id'] = track.get('artistId')
            albums['title'] = track.get('collectionName')
            albums['cover_url'] = track.get('artworkUrl100')
            albums['release_date'] = track.get('releaseDate')
            songs['id'] = track.get('trackId')
            songs['album_id'] = track.get('collectionId')
            songs['title'] = track.get('trackName'),
            songs['duration'] = track.get('trackTimeMillis')
            songs['preview_url'] = track.get('previewUrl')
            belongs['artist_id'] = track.get('artistId')
            belongs['album_id'] = track.get('collectionId')
            contains['album_id'] = track.get('collectionId')
            contains['song_id'] = track.get('trackId')
            try:
                execute_values(self.cur, """
                    INSERT INTO artist (id, name) 
                    VALUES %s;
                """, artists)
                execute_values(self.cur, """
                    INSERT INTO album (id, artist_id, title, cover_url, release_date) 
                    VALUES %s;
                """, albums)
                execute_values(self.cur, """
                    INSERT INTO song (id, album_id, title, duration, preview_url) 
                    VALUES %s;
                """, songs)
                execute_values(self.cur, """
                    INSERT INTO artist_album (artist_id, album_id) 
                    VALUES %s;
                """, belongs)
                execute_values(self.cur, """
                    INSERT INTO album_song (album_id, song_id) 
                    VALUES %s;
                """, belongs)
                self.con.commit()
                print(f'[DB] Bulk load finished. Processed: {len(songs)} songs.')
            except Exception as e:
                self.con.rollback()
                print(f'[DB Error] SQL transaction failed. Rollback applied: {e}')
                raise e
