# Introduction
## What is Phonograph?
Phonograph is a music player inspired on the
one you can use in the gacha game `Honkai Star Rail`, that's where I get the inspiration from to design the UI (That although similar, was repurposed for desktop and mobile clients).\
The particular aspect of this project is not being solely inspired on a gacha game UI, but it also solves a problem I do have as someone of low income; Data usage. People might pay for a cheap data plan that has like 8, 6 or even 4-2 GB of limited usage per month, and as someone who absolutely loves music but changes all the time of likings, it ends up consuming quite a lot of data.

## What does Phonograph do?
This application comes in the play in the before mentioned problem by using a system of countdown that saves every song into a tmp (Temporal) folder and its metadata is saved inside a simple SQLite database, for each day that passes, the countdown goes down and down, and once it reaches 0 the song gets instantly deleted, and if you were to play it again, it would be downloaded once more with the countdown back to normal.\
It doesn't end there though, to be even more efficient, I thought of a way to make it truly <b>count</b>, because with a countdown of 3 days I might be saving data, quite a lot actually, but what if I listen to that particular song for the entire month? <b>Everytime you play the song, the countdown will return to its original value of 3 days</b>, meaning that if you do listen from Monday-Friday a song that you like, you would only have to download it once, no worries whatsoever, you might download it twice or thrice a month maximum if you were to have some holidays or a bridge holiday (Something like no-job from Friday to Sunday).\
And the thing is, you couldn't even be mad, as it saves so much data that you can return to watching videos in YouTube whilst not worrying so much about data usage.

## TL-DR
This is an app that serves as a middle-point from the downloading and streaming songs/music, for those who tend to change with their taste in music.

# Installation and set-up for development

## Python on Linux
### Bash
```bash
python -m venv venv
source venv/bin/activate
pip install -r requeriments.txt
```

### Fish
```bash
python -m venv venv
source venv/bin/activate.fish
pip install -r requeriments.txt
```
## Python on Windows
### CMD
```bash
python -m venv venv
venv\Scripts\activate.bat
pip install -r requeriments.txt
```

### PowerShell
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requeriments.txt
```

# Credits
Author - Breena Lockser\
Packages - yt-dlp, os, sqlite, datetime, shutil\
Documentation - For those heroes that make coding way simpler
