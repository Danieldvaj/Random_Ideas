import os
import re
import sys

def get_timestamp(files):
    """
    Get the latest timestamp from the filenames in a directory.
    """
    date_time_list = []
    for filename in files:
        # search for the date pattern in the filename
        match = re.search(r'\d{8}', filename)
        if match:
            date_time_list.append(match.group())
    return max(date_time_list) if date_time_list else None

def delete_backup(directory):
    """
    Delete all files in a directory that do not contain the latest timestamp in their filename.
    """
    if not os.path.isdir(directory):
        print(f"Directory does not exist: {directory}")
        sys.exit(1)
        
    filenames = os.listdir(directory)
    latest_date = get_timestamp(filenames)

    if not latest_date:
        print("No files found with the expected date format.")
        return

    for filename in filenames:
        if latest_date not in filename:
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
