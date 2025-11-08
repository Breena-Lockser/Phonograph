"""
        youtube.py
---------------------------
Author:     Breena Lockser
Date:       2025-10-30
---------------------------
"""

import yt_dlp as ytdlp
import sql as SQL
import dataManager as data
import os

def download_song(connectionDB, songName, songTitle, videoURL):
    # Setup the options for yt-dlp
    params = {
        # Downloads the best audio format
        'format': 'bestaudio/best',
        # Output file name based on song name
        'outtmpl': f'{songName}.mp3',
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
        ydl.download([videoURL])
        SQL.addSong(connectionDB, songName, songTitle, videoURL, songPath)


def search_video(connectionDB, songName):
    # Setup the options for yt-dlp
    params = {
        # Output file name based on song name
        'outtmpl': f'{songName}.%(ext)s',
        # Set to True to silence output
        'quiet': True,
        # Prevent downloading playlists
        'noplaylist': True,
    }    
    print(f"Searching...")
    with ytdlp.YoutubeDL(params) as ydl:
        # Search and extract only the first result
        result = ydl.extract_info(f"ytsearch1:{songName}", download=False)
        video_url = result['entries'][0]['webpage_url']
        print(f"Found song: {video_url}")
    # Check if the song or video is not way too long. (For storage propuses)
    if result['entries'][0]['duration'] < 300:
        songYoutubeName = result['entries'][0]['title']
        download_song(connectionDB, songName, songYoutubeName, video_url)