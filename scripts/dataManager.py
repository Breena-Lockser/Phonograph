"""
        dataManager.py
---------------------------
Author:     Breena Lockser
Date:       2025-11-18
---------------------------
"""

import sql as SQL
import datetime, os, shutil


# Create all necessary folders for correct usage of the program.
def createFolders():
    dirs = ["tmp", "DBs", "playlists"]
    for folder in dirs:
        path = os.path.join(folder)
        if not os.path.isdir(path):
            os.mkdir(path)


# Checks the date of files in DB.
def check_date(connectionDB):
    date = datetime.datetime.now().strftime("%x")
    try:
        with open("lastDate.txt", "r") as f:
            lastdate = f.readline() 
            f.close()

        if date != lastdate:
            SQL.removeOldSongs(connectionDB)
            SQL.lowerCountdown(connectionDB)
            with open("lastDate.txt", "w") as f:
                f.write(date)
    except:
        with open("lastDate.txt", "w") as f:
            f.write(date)


#region DEBUG ONLY
def debug_reset():
    dirs = ["tmp", "playlists"]
    for folder in dirs:
        root = os.path.join("tmp")
        for filename in os.listdir(root):
            filePath = os.path.join(root, filename)
            try:
                if os.path.isfile(filePath) or os.path.islink(filePath):
                    os.unlink(filePath)
                elif os.path.isdir(filePath):
                    shutil.rmtree(filePath)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (filePath, e))


def restart_database(connectionDB):
    while True:
        userInput = input("Wish to remove all data? (y/n)\n").lower()
        if userInput == "y":
            debug_reset()
            SQL.SQLreset(connectionDB)
            break
        elif userInput == "n":
            break
        else:
            print("Not a valid response.")
#endregion