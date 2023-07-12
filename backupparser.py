import os
import re
import sys

def get_timestamp(directory):
    """
    Get the latest timestamp from the filenames in a directory.
    """
    date_time_list = []
    for filename in os.listdir(directory):
        datetime = re.split('\D+', filename)
        date_time_list.append(datetime[1])
    return sorted(date_time_list)[-1]

def delete_backup(directory):
    """
    Delete all files in a directory that do not contain the latest timestamp in their filename.
    """
    datetime = get_timestamp(directory)
    if not os.path.isdir(directory):
        print(f"Directory does not exist: {directory}")
        sys.exit(1)
    for filename in os.listdir(directory):
        if datetime not in filename:
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
