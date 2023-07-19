import os
import sys

def open_file(file):
    if not os.path.isfile(file):
        print(f"File {file} does not exist.")
        sys.exit(1)
    try:
        with open(file, "r") as file:
            data = file.readlines()
        return data
    except IOError as e:
        print(f"Could not read file {file=}: {str(e)}")
        sys.exit(1)

def parse_data(file):
    data = open_file(file)
    processes = dict()
    for parents in data:
        if parents.startswith("-"):
            parent_process = parents
            processes[parent_process] = None
        elif not parents.startswith('-'):
            processes[parent_process] = parents
    print(processes)


if __name__ == "__main__":
    parse_data("processes.txt")

