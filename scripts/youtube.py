"""
        youtube.py
---------------------------
Author:     Breena Lockser
Date:       2025-10-29
Version:    0.1
---------------------------
"""

import yt_dlp as ytdlp
import sql as SQL
import datetime
import os

def download_song(songName, videoURL):
    # Setup the options for yt-dlp
    params = {
        'format': 'bestaudio/best',  # Downloads the best audio format
        'outtmpl': f'{songName}.%(ext)s',  # Output file name based on song name
        'quiet': True,  # Set to True to silence output
        'noplaylist': True,  # ✅ Prevent downloading playlists
    }
    # Check for existence of the folder, if not, create it.
    folder, folderPath = temporary_folder()
    songPath = os.path.join("tmp", folder, params['outtmpl'])
    params['outtmpl'] = songPath
    # Create an instance of YoutubeDL with the parameters
    with ytdlp.YoutubeDL(params) as ydl:
        # Search and extract only the first result
        ydl.download([videoURL])
        #SQL.addSong(songName, songPath, video_url, folderPath)


def temporary_folder():
    # Get today's date.
    date = datetime.datetime.now()
    # Replace the / with -
    date = date.strftime("%x").replace("/", "-")
    if not os.path.isdir(os.path.join("tmp", date)):
        path = os.path.join("tmp", date)
        os.mkdir(path)
    return date, path


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
    #if result['entries'][0]['genre'] == "music"
        download_song(songName, video_url)
    

search_video("Renegade Hololive")