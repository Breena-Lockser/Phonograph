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
import os


temporal_TUI = """
PHONOGRAPH
-----------
VERSION 0.3
MADE BY Breena Lockser
----------------------

AVAILABLE COMMANDS:

1 - Download a song.
2 - Play music.
3 - Restart the database.
"""


def search_video_user():
    print("Initializing YouTube search...\n")
    while True:
        userInput = input("Song Name: ")
        if len(userInput) == 0:
            print("Please, insert a song name.")
        else:
            break
    YT.search_video(userInput)


def play_music():
    print("\n   Available Songs:\n")
    songs = SQL.listSongs()
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
    songData = SQL.getSongData(userInput)
    print(songData[6])
    input("")


# DEBUG AND TEMPORAL ONLY
def initializeTUI():
    while True:
        print(temporal_TUI)
        userInput = input("Make your choice:\n")
        if len(userInput) == 0:
            print("Please, insert a command ID.")
        else:
            try:
                userInput = int(userInput)
                match userInput:
                    case 1:
                        search_video_user()
                    case 2:
                        play_music()
                    case 2:
                        YT.restart_database()
            except:
                print("Not a valid command ID!")


if __name__ == "__main__":
    initializeTUI()