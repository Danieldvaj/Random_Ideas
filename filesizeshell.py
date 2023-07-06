import shutil
import sys
import logging
import os
from datetime import datetime

def monitor(path):
    if not os.path.exists(path):
        logging.error(f"The path {path} does not exist.")
        sys.exit(1)

    try:
        stat = shutil.disk_usage(path)
    except Exception as e:
        logging.error(f"Failed to get disk usage for {path}: {str(e)}")
        sys.exit(1)

    disk_usage = (stat.used / stat.total) * 100
    logging.info(f"Disk usage for {path}: {disk_usage}%")
    return disk_usage

def log_stats(disk_usage):
    if disk_usage > 80:
        try:
            with open("log.txt", "a") as file:
                file.write(f"{datetime.now()}: Disk usage exceeded 80%. Current usage: {disk_usage}%\n")
        except IOError as e:
            logging.error(f"Failed to write to log file: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py /name/to/path")
        sys.exit(1)

    logging.basicConfig(level=logging.INFO)

    path = sys.argv[1]
    disk_usage = monitor(path)
    log_stats(disk_usage)
