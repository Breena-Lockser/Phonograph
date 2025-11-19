"""
        youtube.py
---------------------------
Author:     Breena Lockser
Date:       2025-11-19
---------------------------
"""

import yt_dlp as ytdlp
import sql as SQL
import dataManager as data
import os


# Search a song by user input.
def search_video(connectionDB, songName):
    # Setup the options for yt-dlp
    params = {
        # Set to True to silence output
        'quiet': True,
        # Prevent downloading playlists
        'noplaylist': True,
    }    
    print(f"Searching...")
    with ytdlp.YoutubeDL(params) as ydl:
        # Search and extract only the first result
        results = ydl.extract_info(f"ytsearch1:{songName}", download=False)
        result = results['entries'][0]
        # Get properties.
        songID = result['id']
        songName = result['title']
        songURL = result['webpage_url']
        songDuration = result['duration']
        channelID = result['channel_id']
        channelName = result['channel']
        channelURL = result['channel_url']
        # Show what was found.
        print("Found song:", songName)
        print("URL:", songURL)
        print("ID:", songID)
        print("From:", channelName)
        print("Channel ID:", channelID)
        # Give the option for the user to say if it's alright.
        while True:
            userInput = input("Is this what you were looking for? (y/n)\n")
            if userInput.lower() == "n":
                return False
            else:
                break
    # Check if the song or song is not way too long. (For storage proposes)
    if songDuration < 300:
        return download_song(connectionDB, songID, songName, songDuration, songURL, channelID, channelName, channelURL)


# Download a song by url.
def download_song(connectionDB, songID, songName, songDuration, songURL, channelID, channelName, channelURL):
    # Setup the options for yt-dlp
    params = {
        # Downloads the best audio format
        'format': 'bestaudio/best',
        # Output file name based on song name
        'outtmpl': f'{songID}.mp3',
        # Set to True to silence output
        'quiet': True,
        # Prevent downloading playlists
        'noplaylist': True,
    }
    # Create a path for the song.
    songPath = os.path.join("tmp", params['outtmpl'])
    params['outtmpl'] = songPath
    print("Downloading...")
    with ytdlp.YoutubeDL(params) as ydl:
        # Search and download only the first result
        ydl.download(songURL)
        if SQL.getArtistID(connectionDB, channelName) == False:
            SQL.addArtist(connectionDB, channelID, channelName, channelURL)
        artistID = SQL.getArtistID(connectionDB, channelName)
        SQL.addSong(connectionDB, songID, songName, songDuration, songURL, songPath, artistID)
    return True