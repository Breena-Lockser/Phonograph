"""
        sql.py
---------------------------
Author:     Breena Lockser
Date:       2025-10-30
---------------------------
"""

import sqlite3 as SQL


# Create or Connect to the database.
def databaseConnection():
    # Connect to the database
    connectionDB = SQL.connect("DBs/Phonograph.db")
    return connectionDB


# Creates the DB tables (Restart the DB if you're a developer.)
def databaseCreation(connectionDB):
    cur = connectionDB.cursor()
    command = """CREATE TABLE IF NOT EXISTS songs(
                    song_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                    song_name TEXT NOT NULL UNIQUE,
                    song_title TEXT NTO NULL UNIQUE,
                    video_url TEXT NOT NULL UNIQUE,
                    countdown INTEGER NOT NULL,
                    path TEXT NOT NULL UNIQUE
                )"""

    cur.execute(command)
    cur.close()
    connectionDB.commit()
    return


# Add a song by using the youtube.py parameters.
def addSong(connectionDB, songName, songTitle, videoURL, path):
    cur = connectionDB.cursor()
    cur.execute("INSERT INTO songs (song_name, song_title, countdown, video_url, path) VALUES (?, ?, ?, ?, ?)", (songName, songTitle, 3, videoURL, path))
    cur.close()

    connectionDB.commit()
    return True


# Remove a song with a certain ID
def removeSong(connectionDB):
    cur = connectionDB.cursor()
    cur.execute("REMOVE FROM songs WHERE song_id = ?", (songName,))
    cur.close()
    connectionDB.commit()
    return


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


# Remove songs with a countdown value of <0>
def removeOldSongs(connectionDB):
    cur = connectionDB.cursor()
    cur.execute("remove FROM songs WHERE countodown = 0")
    cur.close()
    connectionDB.commit()
    return


# Lower by 1 every song countdown (Only done if date has changed.)
def lowerCountdown(connectionDB):
    cur = connectionDB.cursor()
    cur.execute("UPDATE songs SET countdown = countdown - 1")
    cur.close()
    connectionDB.commit()
    return


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


# DEBUG ONLY
def SQLreset(connectionDB):
    cur = connectionDB.cursor()
    cur.execute("DELETE FROM songs")
    cur.close()
    connectionDB.commit()
    return