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

def download_song(songName, songTitle, videoURL):
    # Setup the options for yt-dlp
    params = {
        'format': 'bestaudio/best',  # Downloads the best audio format
        'outtmpl': f'{songName}.mp3',  # Output file name based on song name
        'quiet': True,  # Set to True to silence output
        'noplaylist': True,  # ✅ Prevent downloading playlists
    }
    # Check for existence of the folder, if not, create it.
    folderDate, folderID = data.temporary_folder()
    songPath = os.path.join("tmp", folderDate, params['outtmpl'])
    params['outtmpl'] = songPath
    # Create an instance of YoutubeDL with the parameters
    with ytdlp.YoutubeDL(params) as ydl:
        # Search and extract only the first result
        ydl.download([videoURL])
        SQL.addSong(songName, songTitle, folderDate, folderID, videoURL, songPath)


def search_video(songName):
    # Setup the options for yt-dlp
    params = {
        'format': 'bestaudio/best',  # Downloads the best audio format
        'outtmpl': f'{songName}.%(ext)s',  # Output file name based on song name
        'quiet': True,  # Set to True to silence output
        'noplaylist': True,  # ✅ Prevent downloading playlists
    }    
    # Create an instance of YoutubeDL with the parameters
    with ytdlp.YoutubeDL(params) as ydl:
        # Search and extract only the first result
        result = ydl.extract_info(f"ytsearch1:{songName}", download=False)
        video_url = result['entries'][0]['webpage_url']
        print(f"🎵 Found video: {video_url}")
    if result['entries'][0]['duration'] < 300:
        songYoutubeName = result['entries'][0]['title']
        download_song(songName, songYoutubeName, video_url)