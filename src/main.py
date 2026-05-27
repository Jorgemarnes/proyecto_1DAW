from scraping.scraper import fetch_music_by_artist
from database.loader import DBHandler

def load_data_of(artist_name):
    """Orchestrates the music metadata scraping and loading pipeline."""
    raw_tracks = fetch_music_by_artist(artist_name=artist_name, limit=50)
    if not raw_tracks:
        raise Exception('[Pipeline] No data received from scraper. Aborting pipeline.')
    with DBHandler() as db:
        db.insert_scraped_data(raw_tracks)

if __name__ == '__main__':
    load_data_of(input('Give a artist name to load in the database: '))