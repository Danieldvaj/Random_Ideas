import os
import sys
import time

def check_read_file(filename):
    if not os.path.isfile(filename):
        print(f"File {filename} does not exist.")
        sys.exit(1)
    try:
        with open(filename, "r") as file:
            data = file.readlines()
        return data
    except IOError as e:
        print(f"Could not read file {filename}: {str(e)}")
        sys.exit(1)

def check_status(file):
    file_data = check_read_file(file)
    for error_status in file_data:
        if "error" in error_status.lower():
            date_str = error_status.split('since')[-1].split(';')[0].strip()
            print(f"There was an error at date: {date_str}")
        elif "active: active" in error_status.lower():
            print(".")

if __name__ == "__main__":
    while True:
        check_status("error.log")
        time.sleep(60)
