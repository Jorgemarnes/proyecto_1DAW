You will act as a music data extraction skill specializing in the iTunes Search API.

I need you to retrieve real songs from an artist and save them in a valid, clean JSON format.

## Input Data

```json
{
  "artist_name": "Bad Bunny",
  "limit": 10,
  "country": "ES",
  "language": "es_es"
}
```

## Data Source

Use the endpoint:

```text
https://itunes.apple.com/search
```

With these parameters:

```text
term=<artist_name>
media=music
entity=song
limit=<limit>
country=<country>
lang=<language>
```

## Mandatory rules

1. Return only a valid JSON.
2. Do not add explanations outside of the JSON.
3. Do not fabricate songs, artists, prices, or links.
4. If a field does not exist, write `null`.
5. Remove duplicate songs using `trackId`.
6. Maintain the order received from the API.
7. Convert the duration from milliseconds to seconds using `track_time_seconds`.
8. Use field names in snake_case.
9. If the API does not return any results, return `results: []`.

## Expected structure

```json
[
  {
    "wrapperType": "track",
    "kind": "song",
    "artistId": 32940,
    "collectionId": 269572838,
    "trackId": 269573405,
    "artistName": "Michael Jackson",
    "collectionName": "Thriller",
    "trackName": "Human Nature",
    "collectionCensoredName": "Thriller",
    "trackCensoredName": "Human Nature",
    "artistViewUrl": "https://music.apple.com/us/artist/michael-jackson/32940?uo=4",
    "collectionViewUrl": "https://music.apple.com/us/album/human-nature/269572838?i=269573405&uo=4",
    "trackViewUrl": "https://music.apple.com/us/album/human-nature/269572838?i=269573405&uo=4",
    "previewUrl": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview221/v4/ba/4c/2a/ba4c2a0a-18ff-1350-4ec6-c4e75e053600/mzaf_9049310839196982005.plus.aac.p.m4a",
    "artworkUrl30": "https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/32/4f/fd/324ffda2-9e51-8f6a-0c2d-c6fd2b41ac55/074643811224.jpg/30x30bb.jpg",
    "artworkUrl60": "https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/32/4f/fd/324ffda2-9e51-8f6a-0c2d-c6fd2b41ac55/074643811224.jpg/60x60bb.jpg",
    "artworkUrl100": "https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/32/4f/fd/324ffda2-9e51-8f6a-0c2d-c6fd2b41ac55/074643811224.jpg/100x100bb.jpg",
    "collectionPrice": 9.99,
    "trackPrice": 1.29,
    "releaseDate": "1982-11-29T08:00:00Z",
    "collectionExplicitness": "notExplicit",
    "trackExplicitness": "notExplicit",
    "discCount": 1,
    "discNumber": 1,
    "trackCount": 9,
    "trackNumber": 7,
    "trackTimeMillis": 245838,
    "country": "USA",
    "currency": "USD",
    "primaryGenreName": "Pop",
    "isStreamable": true
  }
]


Now execute the query for the specified artist and return the final JSON populated with the actual API data.