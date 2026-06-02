from src.scraping.scraper import fetch_music_by_artist
from src.ssg.generator import generate_static_site
from src.database.db_handler import DBHandler


def load_data_of(*, db: DBHandler, artist_name: str, limit: int):
    """Orchestrates the music metadata scraping and loading pipeline."""
    raw_tracks = fetch_music_by_artist(artist_name=artist_name, limit=limit)
    if not raw_tracks:
        raise Exception('[Pipeline] No data received from scraper. Aborting operation.')
    db.insert_scraped_data(raw_tracks)

if __name__ == '__main__':
    username = input('Username: ')
    password = input('Password: ')
    with DBHandler(username=username, password=password) as db:
        generate_static_site(db=db)
    if input('Do you want to upload a new artist to de database? (y/n)').lower() == 'y':
        artist_name = input('Artist name: ')
        limit = input('Number of tracks to load (200 max): ')
        if not artist_name:
            raise ValueError('Not artist name recived')
        with DBHandler(username=username, password=password) as db:
            load_data_of(db=db, artist_name=artist_name, limit=int(limit))
            generate_static_site(db=db)
    print('Ending session')