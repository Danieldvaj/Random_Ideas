import os
import sys

def open_file(file_name):
    if not os.path.isfile(file_name):
        print(f"File {file_name} does not exist.")
        sys.exit(1)
    try:
        with open(file_name, "r") as file:
            data = file.readlines()
        return data
    except IOError as e:
        print(f"Could not read file {file_name}: {str(e)}")
        sys.exit(1)

def parse_data(file_name):
    data = open_file(file_name)
    processes = dict()
    parent_process = None
    for line in data:
        line = line.strip()
        if line.startswith("-"):
            parent_process = line[1:]
            processes[parent_process] = []
        elif parent_process is not None:
            processes[parent_process].append(line)
        else:
            print("Error: Found child process without a parent.")
            sys.exit(1)
    print(processes)

if __name__ == "__main__":
    parse_data("processes.txt")
