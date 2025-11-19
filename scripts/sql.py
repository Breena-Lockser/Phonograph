"""
        sql.py
---------------------------
Author:     Breena Lockser
Date:       2025-11-18
---------------------------
"""

import sqlite3 as SQL


#region DB Functions
    # Create or Connect to the database.
def databaseConnection():
    # Connect to the database
    connectionDB = SQL.connect("DBs/Phonograph.db")
    return connectionDB


    # Creates the DB tables (Restart the DB if you're a developer.)
def databaseCreation(connectionDB):
    cur = connectionDB.cursor()
    commands =   ["""CREATE TABLE IF NOT EXISTS songs(
                    song_id TEXT PRIMARY KEY UNIQUE,
                    song_name TEXT NOT NULL UNIQUE,
                    song_artist_id TEXT NOT NULL,
                    video_url TEXT NOT NULL UNIQUE,
                    countdown INTEGER NOT NULL,
                    path TEXT NOT NULL UNIQUE,
                    FOREIGN KEY (song_artist_id) REFERENCES artists(artist_id)
                )""",
                 """CREATE TABLE IF NOT EXISTS artists(
                    artist_id TEXT PRIMARY KEY UNIQUE,
                    artist_name TEXT NOT NULL UNIQUE,
                    artist_url TEXT NOT NULL UNIQUE
                )""",
                 """CREATE TABLE IF NOT EXISTS playlists(
                    playlist_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                    playlist_name TEXT NOT NULL UNIQUE,
                    playlist_path TEXT NOT NULL UNIQUE
                )"""
                ]

    for command in commands:
        cur.execute(command)
    cur.close()
    connectionDB.commit()
    return
#endregion

#region Add ...
    # Add a song by using the youtube.py parameters.
def addSong(connectionDB, songID, songName, songURL, songPath, songArtistID):
    cur = connectionDB.cursor()
    cur.execute("INSERT INTO songs (song_id, song_name, video_url, path, song_artist_id, countdown) VALUES (?, ?, ?, ?, ?, ?)", 
                (songID, songName, songURL, songPath, songArtistID, 3))
    cur.close()

    connectionDB.commit()
    return True


    # Add an artist by using the youtube.py parameters.
def addArtist(connectionDB, artistID, artistName, artistURL):
    cur = connectionDB.cursor()
    cur.execute("INSERT INTO artists (artist_id, artist_name, artist_url) VALUES (?, ?, ?)", (artistID, artistName, artistURL))
    cur.close()

    connectionDB.commit()
    return True


    # Add a playlist by using the desired parameters.
def addPlaylist(connectionDB, playlistName, playlistPath):
    cur = connectionDB.cursor()
    cur.execute("INSERT INTO playlists (playlist_name, playlist_path) VALUES (?, ?)", (playlistName, playlistPath))
    cur.close()

    connectionDB.commit()
    return True
#endregion

#region Remove ...
    # Remove a song with a certain ID
def removeSong(connectionDB, songID):
    cur = connectionDB.cursor()
    cur.execute("REMOVE FROM songs WHERE song_id = ?", (songID,))
    cur.close()
    connectionDB.commit()
    return


    # Remove songs with a countdown value of <0>
def removeOldSongs(connectionDB):
    cur = connectionDB.cursor()
    cur.execute("remove FROM songs WHERE countodown = 0")
    cur.close()
    connectionDB.commit()
    return

    # Remove a playlist with a certain ID
def removePlaylist(connectionDB, playlistID):
    cur = connectionDB.cursor()
    cur.execute("REMOVE FROM playlists WHERE playlist_id = ?", (playlistID,))
    cur.close()
    connectionDB.commit()
    return

    # Remove a song with a certain ID
def removeArtist(connectionDB, artistID):
    cur = connectionDB.cursor()
    cur.execute("REMOVE FROM artists WHERE artist_id = ?", (artistID,))
    cur.close()
    connectionDB.commit()
    return
#endregion

#region List ...
    # List all songs in the songs table in DB.
def listSongs(connectionDB):
    cur = connectionDB.cursor()
    cur.execute("SELECT * from songs")
    try:
        songs = cur.fetchall()
        cur.close()
        return songs
    except:
        return False


    # List all songs in the songs table in DB.
def listArtists(connectionDB):
    cur = connectionDB.cursor()
    cur.execute("SELECT * from artists")
    try:
        artists = cur.fetchall()
        cur.close()
        return artists
    except:
        return False


    # List all playlists in the playlists table in DB.
def listPlaylists(connectionDB):
    cur = connectionDB.cursor()
    cur.execute("SELECT * from playlists")
    try:
        playlists = cur.fetchall()
        cur.close()
        return playlists
    except:
        return False
#endregion

#region Get data from...
    # Check all song data from a song with a certain ID.
def getSongData(connectionDB, songID):
    cur = connectionDB.cursor()
    cur.execute("SELECT * from songs where song_id = ?", (songID,))
    try:
        songData = cur.fetchone()
        cur.close()
        return songData
    except:
        return False


    # Check all artist data from an artist with a certain ID.
def getArtistData(connectionDB, artistID):
    cur = connectionDB.cursor()
    cur.execute("SELECT * from artists where artist_id = ?", (artistID,))
    try:
        artistData = cur.fetchone()
        cur.close()
        return artistData
    except:
        return False


    # Check all artist data from an artist with a certain ID.
def getPlaylistData(connectionDB, playlistID):
    cur = connectionDB.cursor()
    cur.execute("SELECT * from playlists where playlist_id = ?", (playlistID,))
    try:
        playlistData = cur.fetchone()
        cur.close()
        return playlistData
    except:
        return False
#endregion

#region Get ID from...
def getSongID(connectionDB, songName):
    cur = connectionDB.cursor()
    cur.execute("SELECT * from songs where song_name = ?", (songName,))
    try:
        songID = cur.fetchone()
        cur.close()
        return songID
    except:
        return False


    # Check all artist data from an artist with a certain ID.
def getArtistID(connectionDB, artistName):
    cur = connectionDB.cursor()
    cur.execute("SELECT * from artists where artist_name = ?", (artistName,))
    try:
        artistID = cur.fetchone()[0]
        cur.close()
        return artistID
    except:
        return False


    # Check all artist data from an artist with a certain ID.
def getPlaylistID(connectionDB, playlistName):
    cur = connectionDB.cursor()
    cur.execute("SELECT * from playlists where playlist_name = ?", (playlistName,))
    try:
        playlistID = cur.fetchone()
        cur.close()
        return playlistID
    except:
        return False
#endregion

#region Miscellaneous
    # Lower by 1 every song countdown (Only done if date has changed.)
def lowerCountdown(connectionDB):
    cur = connectionDB.cursor()
    cur.execute("UPDATE songs SET countdown = countdown - 1")
    cur.close()
    connectionDB.commit()
    return
#endregion

#region DEBUG ONLY
def SQLreset(connectionDB):
    cur = connectionDB.cursor()
    cur.execute("DELETE FROM songs")
    cur.close()
    connectionDB.commit()
    return
#endregion