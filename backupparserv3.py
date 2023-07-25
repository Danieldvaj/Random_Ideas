import os
import re
from datetime import datetime

def get_dates_and_files(directory):
    """
    Get the dates from the filenames in a directory and return a dictionary with filenames as keys and dates as values.
    """
    file_date_dict = {}
    for filename in os.listdir(directory):
        match = re.search(r'\d{8}', filename)
        if match:
            date = datetime.strptime(match.group(), '%Y%m%d')
            file_date_dict[filename] = date
    return file_date_dict

def delete_backup(directory):
    """
    Delete all files in a directory that do not contain the latest date in their filename.
    """
    file_date_dict = get_dates_and_files(directory)
    if not file_date_dict:
        print("No files found with the expected date format.")
        return

    latest_file = max(file_date_dict, key=file_date_dict.get)
    for filename in os.listdir(directory):
        if filename != latest_file:
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                try:
                    os.remove(file_path)
                    print(f"Succesfully removed {filename}")
                except OSError as e:
                    print(f"Failed to remove {filename}: {str(e)}")
            else:
                print(f"File does not exist: {filename}")

delete_backup("./backup/")
