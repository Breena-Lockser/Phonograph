"""
        dataManager.py
---------------------------
Author:     Breena Lockser
Date:       2025-10-30
---------------------------
"""

import sql as SQL
import datetime, os, shutil


def temporary_folder():
    # Get today's date.
    date = datetime.datetime.now().strftime("%x")
    check_date(date)
    try:
        folderData = SQL.checkFolder(date.replace("/", "-"))
        if folderData == False:
            # Replace the / with -
            date = date.replace("/", "-")
            if not os.path.isdir(os.path.join("tmp", date)):
                path = os.path.join("tmp", date)
                os.mkdir(path)
                if SQL.addFolder(date, path):
                    folderData = SQL.checkFolder(date)
                    print(folderData)
            return date, folderData[0]
        else:
            folderID, folderDate = folderData[0], folderData[1]
            return folderDate, folderID
    except:
        # Replace the / with -
        date = date.replace("/", "-")
        if not os.path.isdir(os.path.join("tmp", date)):
            path = os.path.join("tmp", date)
            os.mkdir(path)
            if SQL.addFolder(date, path):
                folderData = SQL.checkFolder(date)
                print(folderData)
        return date, folderData[0]


def check_date(date):
    try:
        with open("lastDate.txt", "r") as f:
            lastdate = f.readline() 
            f.close()

        if date != lastdate:
            foldersData = SQL.checkAllFolders()
            print(foldersData)
            with open("lastDate.txt", "w") as f:
                f.write(date)
    except:
        with open("lastDate.txt", "w") as f:
            f.write(date)


# DEBUG ONLY
def debug_reset():
    SQL.SQLreset()
    root = "tmp"
    for folder in os.listdir(os.path.join(root)):
        print("In directory {}".format(folder))
        folderDir = os.path.join(root, folder)
        if os.path.isdir(folderDir):
            shutil.rmtree(folderDir)
            print(folderDir, "has been removed") 
        else:
            print(folderDir, "is not a dir.")

# DEBUG ONLY
def restart_database():
    SQL.databaseCreation()
    while True:
        userInput = input("Wish to remove all data? (y/n)\n").lower()
        if userInput == "y":
            debug_reset()
            break
        elif userInput == "n":
            break
        else:
            print("Not a valid response.")