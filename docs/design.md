# Static Page Structure Documentation

## Overview

This generator creates a static music store discography page using the data stored in the database. The page displays artists, their albums, album covers, release years, generated prices, and the list of songs for each album.

The generator produces two output files:

* An HTML file, defined by `SS_URL`.
* A CSS stylesheet, defined by `SS_STYLE_URL`.

The generated page is a static website, meaning that once the files are created, the content can be displayed directly by a browser without needing a backend server to render the page dynamically.

---

## Data Source

The generator receives a database handler object called `db`. It uses the method:

```python
db.fetch_distinct_albums()
```

This method is expected to return album information with the following values:

```text
artist, album, cover, release, songs
```

Each item represents:

* `artist`: Name of the artist.
* `album`: Album title.
* `cover`: URL of the album cover image.
* `release`: Album release year.
* `songs`: A string containing the songs of the album.

The songs are separated by semicolons. Each song contains a title and a duration in milliseconds.

Example format:

```text
Song title,210000;Another song,185000
```

The generator converts each duration from milliseconds into a readable `mm:ss` format.

---

## HTML Page Structure

The generated HTML page follows this general structure:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Music Store Discography</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Music Store</h1>
            </div>

            <div class="content">
                <!-- Artists are inserted here dynamically -->
            </div>
        </div>
    </body>
</html>
```

---

## Main Layout

### 1. Container

The `.container` element wraps the whole visible page content.

Its purpose is to center the page and limit the maximum width of the content.

```html
<div class="container">
    ...
</div>
```

In the CSS, it has a maximum width of `1200px` and is centered horizontally with automatic margins.

---

### 2. Header

The `.header` section contains the main title of the page:

```html
<div class="header">
    <h1>Music Store</h1>
</div>
```

This section is centered and visually separated from the rest of the content using margins.

---

### 3. Content Section

The `.content` section contains all the generated artist blocks.

```html
<div class="content">
    <!-- Artist blocks -->
</div>
```

Each artist is represented by an individual card.

---

## Artist Block Structure

Each artist is displayed inside a `.artist` container.

```html
<div class="artist">
    <h2>Artist Name</h2>

    <!-- Album blocks -->
</div>
```

The artist block works as a card. It has:

* White background.
* Rounded corners.
* Internal padding.
* Box shadow.
* Bottom margin between artists.

The artist name is displayed with an `<h2>` heading and styled using the main accent color.

---

## Album Block Structure

Each album is displayed inside an `.album` container.

```html
<div class="album">
    <img src="album-cover-url" alt="Album cover">

    <div class="album-info">
        <h3>
            <div>
                Album Title <span class="year">(Release Year)</span>
            </div>
            <span class="price">15.99€</span>
        </h3>

        <ul class="song-list">
            <!-- Songs -->
        </ul>
    </div>
</div>
```

The album block contains:

* Album cover image.
* Album title.
* Release year.
* Randomly generated price.
* Song list.

The `.album` layout uses flexbox, placing the album cover on the left and the album information on the right.

---

## Album Cover

The album cover is displayed using an `<img>` tag.

```html
<img src="cover-url" alt="Portada de Album Title">
```

The CSS gives the image:

* Fixed width of `150px`.
* Fixed height of `150px`.
* Rounded corners.
* `object-fit: cover`, so the image fills the square area without distortion.
* A subtle shadow.

---

## Album Information

The `.album-info` section contains the textual information of the album.

```html
<div class="album-info">
    ...
</div>
```

This section expands to fill the remaining horizontal space next to the album image.

The album title and price are displayed in the same row using flexbox.

---

## Release Year

The release year is displayed inside a span with the class `.year`.

```html
<span class="year">(2024)</span>
```

It is styled in grey to make it visually secondary compared to the album title.

---

## Price

The album price is displayed inside a span with the class `.price`.

```html
<span class="price">14.99€</span>
```

The price is generated randomly between 10 and 20 euros using Python.

It is styled in dark red to make it stand out.

---

## Song List Structure

Each album contains a song list.

```html
<ul class="song-list">
    <li class="song-item">
        <span class="song-title">Song Title</span>
        <span class="song-duration">3:45</span>
    </li>
</ul>
```

Each song item contains:

* Song title.
* Song duration.

The duration is shown in `minutes:seconds` format.

---

## Song Item Layout

Each `.song-item` uses flexbox to separate the song title and the duration.

The title is aligned to the left, while the duration is aligned to the right.

A dashed bottom border is used to visually separate each song.

The last song item removes the bottom border.

---

## CSS Structure

The stylesheet starts with CSS variables:

```css
:root {
    --bg-color: lightgrey;
    --text: black;
    --border: grey;
    --accent: darkblue;
}
```

These variables define the main visual theme of the page:

* `--bg-color`: Background color of the page.
* `--text`: Main text color.
* `--border`: Border and secondary text color.
* `--accent`: Main highlight color.

---

## Visual Design

The generated page uses a simple card-based layout.

Main design features:

* Light grey background.
* White artist cards.
* Rounded corners.
* Soft shadows.
* Dark blue accent color for artist names.
* Dark red color for prices.
* Flexbox layout for album rows.
* Clean song list with separated title and duration.

This design makes the discography easy to read and gives the page the appearance of a simple music store catalogue.

---

## Generated Page Hierarchy

The complete visual hierarchy is:

```text
Music Store page
│
├── Header
│ └── Page title
│
└── Content
    │
    ├── Artist card
    │ ├── Artist name
    │ │
    │ ├── Album
    │ │ ├── Album cover
    │ │ └── Album information
    │ │ ├── Album title
    │ │ ├── Release year
    │ │ ├── Price
    │ │ └── Song list
    │ │ ├── Song title
    │ │ └── Song duration
    │ │
    │ └── More albums
    │
    └── More artists
```

---

## Error Handling

If the database does not return any valid artist data, the generator raises an error:

```python
ValueError('No artist fetch from the database')
```

This prevents the program from generating an empty page without useful content.

---

## Summary

This generator builds a complete static music catalogue page from database content. It groups albums by artist, formats song durations, creates the HTML structure, and writes the CSS styles automatically.

The final result is a static webpage that displays:

* Artists.
* Albums.
* Album covers.
* Release years.
* Prices.
* Songs.
* Song durations.

The page is suitable for a simple music store, catalogue, or discography viewer.