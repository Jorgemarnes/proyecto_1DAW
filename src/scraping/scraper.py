import requests
from requests.exceptions import RequestException
from config import BASE_URL

def fetch_music_by_artist(*, artist_name: str, limit: int = 50) -> list:
    """Get songs data from the Itunes API."""
    url = f'{BASE_URL}search'
    params = {
        'term': artist_name,
        'media': 'music',
        'limit': limit
    }
    try:
        with requests.get(url, params=params, timeout=10) as response:
            response.raise_for_status()
            return response.json().get('results', [])
    except RequestException as e:
        print(f"[Red Error] Can not connect to iTunes: {e}")
        return []

if __name__ == '__main__':
    
    print(fetch_music_by_artist(artist_name='Michael Jackson', limit=2))