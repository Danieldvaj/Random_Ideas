import sys
import os

def word_count(*files):
    for fname in files:
        if os.path.isfile(fname):
            with open(fname) as f:
                lines = f.readlines()
                line_count = len(lines)
                word_count = sum(len(line.split()) for line in lines)
                char_count = sum(len(line) for line in lines)
            print(f"For file {fname}: Lines: {line_count}, Words: {word_count}, Characters: {char_count}")
        else:
            print(f"{fname} does not exist.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py file1 file2 ...")
        sys.exit(1)

    files = sys.argv[1:]
    word_count(*files)
