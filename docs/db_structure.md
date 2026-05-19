# Database Schema Documentation

This document describes the relational database schema derived from the Entity-Relationship (ER) diagram for the music platform.

[ER diagram](/src/database/modelo_relacional.png)

<br>

## Entities and Attributes

### 1. User
Represents the registered users on the platform.
*   `id` (INT, PK): Unique identifier for the user.
*   `name` (VARCHAR): Unique username.
*   `email` (VARCHAR): User's email address (underlined/unique).
*   `password` (VARCHAR): Hashed user password.
*   `log_date` (DATE/DATETIME): Timestamp of when the user registered.

<br>

### 2. Artist
Represents the music creators or bands.
*   `id` (INT, PK): Unique identifier for the artist.
*   `name` (VARCHAR): Stage name or group name.
*   `bio` (TEXT): Biography details of the artist.
*   `profile_pic_url` (VARCHAR): URL linking to the artist's profile picture.

<br>

### 3. Song
Represents individual audio tracks available on the platform.
*   `id` (INT, PK): Unique identifier for the song.
*   `title` (VARCHAR): Title of the track.
*   `duration` (INT): Duration of the song in seconds.
*   `archive_url` (VARCHAR): URL path pointing to the audio file storage.
*   `album_id` (INT, FK): Reference to the album this song belongs to.

<br>

### 4. Album
Represents a collection of songs published together.
*   `id` (INT, PK): Unique identifier for the album.
*   `title` (VARCHAR): Title of the album.
*   `cover_url` (VARCHAR): URL linking to the album cover image.
*   `release_date` (DATE): Official release date.
*   `artist_id` (INT, FK): Reference to the main artist who created the album.

<br>

## Relationships and Cardinalities

### 1. Buy | User <-> Album
A many-to-many (**N:M**) relationship tracking album purchases by users.
*   **Cardinality:** A `user` can buy 0 to many `(0,n)` albums. An `album` can be bought by 0 to many `(0,m)` users.
*   **Implementation:** Requires a junction table (`user_buy_album`) containing:
    *   `user_id` (FK)
    *   `album_id` (FK)

<br>

### 2. Belong | Artist <-> Album
A many-to-many (**N:M**) relationship mapping collaboration or ownership between artists and albums.
*   **Cardinality:** An `artist` can have 1 to many `(1,n)` albums. An `Álbum` can belong to 1 to many `(1,m)` artists.
*   **Implementation:** Requires a junction table (`album_belongs_artist`) containing:
    *   `artist_id` (FK)
    *   `album_id` (FK)

<br>

### 3. Contain | Song <-> Album
The diagram specifies a many-to-many (**N:M**) relationship here, though structurally standard tracks usually belong to one album. Based strictly on the visual indicators:
*   **Cardinality:** A `song` belongs to 1 to many (`1,n`) albums. An `Álbum` contains 1 to many (`1,m`) songs.
*   **Implementation:** Requires a junction table (`Album_Contener_Cancion`) containing:
    *   `id_album` (FK)
    *   `id_cancion` (FK)

