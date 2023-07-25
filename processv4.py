import re
import os
import sys

def read_data(filename):
    # Check if the file exists and can be read
    if not os.path.isfile(filename) or not os.access(filename, os.R_OK):
        print(f"File cannot be read: {filename}")
        sys.exit(1)

    with open(filename, "r") as file_data:
        data = file_data.readlines()
        # Check if file is not empty
        if not data:
            print("File is empty.")
            sys.exit(1)

        print("Parsing process-list")
        return data

def count_processes(data):
    process_data = [line for line in data if not "PID COMMAND" in line]
    print(f"Total processes: {len(process_data)}")

def user_invoked(data):
    count = 0
    for line in data:
        # Check if line format is correct
        try:
            if len(line) - len(re.sub(r'(\d+)\s+(\\_)', r'\1\2', line)) >= 5:
                count += 1
        except re.error as e:
            print(f"Error processing line: {str(e)}")
    print(f"User processes {count}")

def count_scripts(data):
    scripts = {}
    for line in data:
        # Check if line format is correct
        try:
            match = re.search(r'(\./[^ \)]*\.[^ \)]+)', line)
            if match:
                amount = match.group()
                scripts[amount] = scripts.get(amount, 0) + 1
        except re.error as e:
            print(f"Error processing line: {str(e)}")

    print("Active scripts:")
    for amount, count in scripts.items():
        print(f"    {count}x {amount}")


if __name__ == "__main__":
    data = read_data('process-list.txt')
    count_processes(data)
    user_invoked(data
