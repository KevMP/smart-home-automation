import shutil
from datetime import datetime
import time

def getCurrentTime():
    return datetime.now()

def formatTime(current_time):
    # Formats the datetime object as a string (e.g., '2023-12-20_13-45-30')
    return current_time.strftime('%m-%d-%Y_%H')

def writeNewDatabaseWithTime(current_time):
    formatted_time = formatTime(current_time)
    shutil.copyfile('./local/database.db', f'./local/database_backups/database_{formatted_time}.db')

def backupDatabaseEveryHour():
    current_time = getCurrentTime()
    writeNewDatabaseWithTime(current_time)
    time.sleep(3600)  # 1 hour (3600 seconds)

if __name__ == "__main__":
    while True:
        for hour in range(24):
            backupDatabaseEveryHour()
        print("NEW DAY HAS ELAPSED, 24 BACKUPS HAVE BEEN MADE")