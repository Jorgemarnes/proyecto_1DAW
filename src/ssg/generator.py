from src.database.db_handler import DBHandler
from src.settings.settings import SS_URL, SS_STYLE_URL

def format_duration(millis_str: str) -> str:
    """Convert the miliseconds to mm:ss format"""
    millis = int(millis_str)
    seconds = (millis // 1000) % 60
    minutes = (millis // (1000 * 60)) % 60
    return f'{minutes}:{seconds:02d}'


def generate_static_site(*, db: DBHandler):
    """Generates a static HTML page with the disticts artists discography saved in the database."""
    data = []
    artist_data = {}
    for artist, album, cover, release, songs in db.fetch_distinct_albums():
        if not artist:
            continue
        if artist not in artist_data:
            artist_data[artist] = {'artist': artist, 'albums': []}
        album_entry = {
            'title': album,
            'release': release,
            'cover': cover,
            'songs': []
        }
        for song in songs.split(';'):
            title, duration = song.rsplit(',', 1)
            songs_entry = {
                'title': title,
                'duration': format_duration(duration)
            }
            album_entry['songs'].append(songs_entry)
        artist_data[artist]['albums'].append(album_entry)
    if not artist_data:
        raise ValueError('No artist fetch from the database')
    data = list(artist_data.values())
    
    artists_html = []
    for artist_info in data:
        artists_html.append(f"""
                <div class='artist'>\n<h2>{artist_info['artist']}</h2>
        """)
        for album in artist_info['albums']:
            artists_html.append(f"""
                    <div class='album'>
                        <img src="{album['cover']}" alt="Portada de {album['title']}">
                        <div class='album-info'>
                            <h3>{album['title']} <span class='year'>({album['release']})</span></h3>
                            <ul class='song-list'>
            """)
            for song in album['songs']:
                artists_html.append(f"""
                                <li class='song-item'>
                                    <span class='song-title'>{song['title']}</span>
                                    <span class='song-duration'>{song['duration']}</span>
                                </li>
                """)
            artists_html.append("""
                            </ul>
                        </div>
                    </div>
            """)
        artists_html.append("""
                </div>
        """)
    with open(SS_URL, 'w') as f:
        f.write(f"""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Music Store Discography</title>
        <link rel="stylesheet" href={SS_STYLE_URL}>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Music Store</h1>
            </div>
            <div class="content">
                {''.join(artists_html)}
            </div>
        </div>
    </body>
</html>
""")
    with open(SS_STYLE_URL, 'w') as f:
        f.write("""
:root {
    --bg-color: #f4f4f9;
    --text: #333;
    --border: #e2e8f0;
    --accent: #3b82f6;
}
body {
    font-family: system-ui,
    -apple-system, sans-serif;
    background-color: var(--bg-color);
    color: var(--text);
    padding: 2rem;
    margin: 0;
}
.header {
    text-align: center;
    margin-bottom: 3rem;
}
.container {
    max-width: 900px;
    margin: 0 auto;
}
.artist {
    background: white;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    margin-bottom: 2rem;
}
.artist h2 {
    margin-top: 0;
    color: var(--accent);
    border-bottom: 2px solid var(--border);
    padding-bottom: 0.5rem;
}
.album {
    display: flex;
    gap: 1.5rem;
    margin-top: 1.5rem;
    padding-top: 1.5rem;
    border-top: 1px solid var(--border);
}
.album img {
    width: 120px;
    height: 120px;
    border-radius: 8px;
    object-fit: cover;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.album-info {
    flex-grow: 1;
}
.album-info h3 {
    margin: 0 0 1rem 0;
    font-size: 1.2rem;
}
.year {
    color: #64748b;
    font-weight: normal;
    font-size: 1rem;
}
.song-list {
    list-style: none;
    padding: 0;
    margin: 0;
}
.song-item {
    display: flex;
    justify-content: space-between;
    padding: 0.5rem 0;
    border-bottom: 1px dashed var(--border);
    font-size: 0.95rem;
}
.song-item:last-child {
    border-bottom: none;
}
.song-duration {
    color: #64748b;
    font-family: monospace;
    font-size: 1rem;
}
""")
    print(f'Static site generated succesfully at {SS_URL}')