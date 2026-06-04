Actúa como una skill de extracción de datos musicales especializada en la API pública de iTunes Search API.

Necesito que obtengas canciones reales de un artista y las guardes en un JSON válido y limpio.

## Datos de entrada

```json
{
  "artist_name": "Bad Bunny",
  "limit": 10,
  "country": "ES",
  "language": "es_es"
}
```

## Fuente de datos

Usa el endpoint:

```text
https://itunes.apple.com/search
```

Con estos parámetros:

```text
term=<artist_name>
media=music
entity=song
limit=<limit>
country=<country>
lang=<language>
```

## Reglas obligatorias

1. Devuelve únicamente JSON válido.
2. No añadas explicaciones fuera del JSON.
3. No inventes canciones, artistas, precios ni enlaces.
4. Si un campo no existe, escribe `null`.
5. Elimina canciones duplicadas usando `trackId`.
6. Mantén el orden recibido desde la API.
7. Convierte la duración de milisegundos a segundos en `track_time_seconds`.
8. Usa nombres de campos en snake_case.
9. Si la API no devuelve resultados, devuelve `results: []`.

## Estructura exacta esperada

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


Ahora ejecuta la consulta para el artista indicado y devuelve el JSON final poblado con los datos reales de la API.