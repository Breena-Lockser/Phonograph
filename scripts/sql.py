"""
        sql.py
---------------------------
Author:     Breena Lockser
Date:       2025-10-30
---------------------------
"""

import sqlite3 as SQL

# Connect to the database
connection = SQL.connect("DBs/Phonograph.db")


def databaseCreation():
    cur = connection.cursor()
    
    commands = [
        """CREATE TABLE IF NOT EXISTS songs(
            song_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            song_name TEXT NOT NULL UNIQUE,
            folder_date TEXT NOT NULL,
            folder_id INTEGER,
            video_url TEXT NOT NULL UNIQUE,
            path TEXT NOT NULL UNIQUE,
            FOREIGN KEY(folder_id) REFERENCES maps(folder_id)
        )""",
        """CREATE TABLE IF NOT EXISTS folders(
            folder_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            date TEXT NOT NULL UNIQUE,
            path TEXT NOT NULL UNIQUE,
            countdown INTEGER NOT NULL
        )"""
    ]

    for command in commands:
        cur.execute(command)
    
    cur.close()
    connection.commit()


def addSong(songName, folderDate, folderID, videoURL, path):
    cur = connection.cursor()
    cur.execute("INSERT INTO songs (song_name, folder_date, folder_id, video_url, path) VALUES (?, ?, ?, ?, ?)", (songName, folderDate, folderID, videoURL, path))
    cur.close()

    connection.commit()
    return True


def removeSong():
    # TO-DO
    pass


def listSongs():
    cur = connection.cursor()
    cur.execute("SELECT * from songs")
    try:
        songs = cur.fetchall()
        cur.close()
        return songs
    except:
        return False


def addFolder(folderDate, path):
    cur = connection.cursor()
    cur.execute("INSERT INTO folders (date, path, countdown) VALUES (?, ?, ?)", (folderDate, path, 3))
    cur.close()

    connection.commit()
    return True


def removeFolder(folderID):
    cur = connection.cursor()
    try:
        cur.execute("REMOVE FROM folders WHERE folder_id = (?)", (folderID,))
        cur.close()

        connection.commit()
        return True
    except:
        print("The folder doesn't exist!")
        cur.close()
        return False


def checkFolder(folderDate):
    cur = connection.cursor()
    cur.execute("SELECT * FROM folders WHERE date = ?", (folderDate,))
    try:
        folderData = cur.fetchone()
        cur.close()
        return folderData
    except:
        return False


def checkAllFolders():
    cur = connection.cursor()
    cur.execute("SELECT * from folders")
    try:
        folders = cur.fetchall()[0]
        cur.close()
        return folders
    except:
        return False
    

# DEBUG ONLY
def SQLreset():
    cur = connection.cursor()
    commands = [
        "DELETE FROM folders",
        "DELETE FROM songs"
    ]
    for command in commands:
        cur.execute(command)
    cur.close()


if __name__ == '__main__':
    databaseCreation()