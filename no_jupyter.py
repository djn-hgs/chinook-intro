import sqlite3 as sql

with sql.connect('db.sqlite') as db:
    c = db.cursor()

    album_artist_track_genre_query = '''
    SELECT Album.Title, Artist.Name, Track.Name, Genre.Name
    FROM Album
    INNER JOIN Artist
    INNER JOIN Track
    INNER JOIN Genre
    WHERE Album.ArtistID = Artist.ArtistID
    AND Track.AlbumID = Album.AlbumID
    AND Track.GenreID = Genre.GenreID
    AND Genre.Name IS 'Soundtrack'
    '''

    c.execute(album_artist_track_genre_query)
    albums = c.fetchall()

    for line in albums:
        print(line)

