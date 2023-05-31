import sys
import os

def replace_string(directory, extension, old_string, new_string):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    file_data = f.read()
                file_data = file_data.replace(old_string, new_string)
                with open(file_path, 'w') as f:
                    f.write(file_data)
                print(f"Replaced '{old_string}' with '{new_string}' in: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py directory extension old_string new_string")
        sys.exit(1)

    directory = sys.argv[1]
    extension = sys.argv[2]
    old_string = sys.argv[3]
    new_string = sys.argv[4]
    replace_string(directory, extension, old_string, new_string)
