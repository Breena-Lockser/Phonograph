"""
        control.py
---------------------------
Author:     Breena Lockser
Date:       2025-10-30
Version:    0.3
---------------------------
"""

import youtube as YT
import sql as SQL
import vlc


def search_video_user():
    while True:
        user_input = input("Song Name: ")
        if len(user_input) == 0:
            print("Please, insert a song name.")
        else:
            break
    YT.search_video(user_input)


def play_music():
    songs = SQL.listSongs()
    availableSongs = []
    for song in songs:
        availableSongs.append(song[0])
        print(song[0], song[1])
    while True:
        user_input = input("Song ID: ")
        if len(user_input) == 0:
            print("Please, insert a song ID.")
        else:
            try:
                user_input = int(user_input)
            except:
                print("Not a valid ID!")
            break
    # SEARCH FOR THE SONG WITH THE SELECTED ID (GET PATH)
    # p = vlc.MediaPlayer("file:///path/to/track.mp3")
    # p.play()


play_music()
search_video_user()