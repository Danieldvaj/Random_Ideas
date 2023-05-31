import sys
import os
import shutil

def move_files(extension, source_directory, destination_directory):
    if not os.path.isdir(destination_directory):
        os.makedirs(destination_directory)

    for root, dirs, files in os.walk(source_directory):
        for file in files:
            if file.endswith(extension):
                shutil.move(os.path.join(root, file), destination_directory)
                print(f"Moved {file} to {destination_directory}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py extension source_directory destination_directory")
        sys.exit(1)

    extension = sys.argv[1]
    source_directory = sys.argv[2]
    destination_directory = sys.argv[3]
    move_files(extension, source_directory, destination_directory)
