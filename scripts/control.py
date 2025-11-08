"""
        control.py
---------------------------
Author:     Breena Lockser
Date:       2025-10-30
Version:    0.35
---------------------------
"""

import youtube as YT
import sql as SQL
import dataManager
import os


temporal_TUI = """
PHONOGRAPH
-----------
VERSION 0.4
MADE BY Breena Lockser
----------------------

AVAILABLE COMMANDS:

1 - Download a song.
2 - Play music.
3 - Restart the database.
9 - Exit.
"""


# Asks for a valid song name to search in youtube.py
def search_video_user(connectionDB):
    print("Initializing YouTube search...\n")
    while True:
        userInput = input("Song Name: ")
        if len(userInput) == 0:
            print("Please, insert a song name.")
        else:
            break
    YT.search_video(connectionDB, userInput)


# As mentioned in commits, I will refrain from 
# using VLC/MPV/pygame because react will be the one doing the work.
# This only shows the song path.
def play_music(connectionDB):
    print("\n   Available Songs:\n")
    songs = SQL.listSongs(connectionDB)
    if songs == []:
        print("No songs in database!")
        input("Press anything to continue.")
        return
    availableSongs = []
    for song in songs:
        availableSongs.append(song[0])
        print(song[0], song[2])
    while True:
        userInput = input("Song ID: ")
        if len(userInput) == 0:
            print("Please, insert a song ID.")
        else:
            try:
                userInput = int(userInput)
                break
            except:
                print("Not a valid ID!")
    songData = SQL.getSongData(connectionDB, userInput)
    print("Path:", songData[5])
    input("Press anything to continue.")


# DEBUG AND TEMPORAL ONLY
def initializeTUI(connectionDB):
    while True:
        print(temporal_TUI)
        userInput = input("Make your choice:\n")
        if len(userInput) == 0:
            print("Please, insert a command ID.")
        else:
            try:
                userInput = int(userInput)
                if userInput == 9:
                    break
                commandInitialization(userInput, connectionDB)
            except:
                print("Not a valid ID.")


# Manages the id given by the user.
def commandInitialization(commandID, connectionDB):
    match commandID:
        case 1:
            search_video_user(connectionDB)
        case 2:
            play_music(connectionDB)
        case 3:
            dataManager.restart_database(connectionDB)


if __name__ == "__main__":
    # Check for folders (Such as DBs and tmp).
    dataManager.createFolders()
    # Connect to the DB and create a table if not existent.
    connectionDB = SQL.databaseConnection()
    SQL.databaseCreation(connectionDB)
    # Check for different date
    dataManager.check_date(connectionDB)
    # Initialize the terminal interface for interaction.
    initializeTUI(connectionDB)