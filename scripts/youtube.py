"""
Youtube API handler.
V0.2
"""

import yt_dlp as ytdlp

def download_song(song_name, video_url):
    # Setup the options for yt-dlp
    params = {
        'format': 'bestaudio/best',  # Downloads the best audio format
        'outtmpl': f'tmp/{song_name}.%(ext)s',  # Output file name based on song name
        'quiet': True,  # Set to True to silence output
        'noplaylist': True,  # ✅ Prevent downloading playlists
    }
    # Create an instance of YoutubeDL with the parameters
    with ytdlp.YoutubeDL(params) as ydl:
        # Search and extract only the first result
        ydl.download([video_url])


def temporary_folder():
    pass


def search_video(song_name):
    # Setup the options for yt-dlp
    params = {
        'format': 'bestaudio/best',  # Downloads the best audio format
        'outtmpl': f'{song_name}.%(ext)s',  # Output file name based on song name
        'quiet': True,  # Set to True to silence output
        'noplaylist': True,  # ✅ Prevent downloading playlists
    }    
    # Create an instance of YoutubeDL with the parameters
    with ytdlp.YoutubeDL(params) as ydl:
        # Search and extract only the first result
        result = ydl.extract_info(f"ytsearch1:{song_name}", download=False)
        video_url = result['entries'][0]['webpage_url']
        print(f"🎵 Found video: {video_url}")
    if result['entries'][0]['duration'] < 240:
        download_song(song_name, video_url)


search_video("Renegade Hololive")