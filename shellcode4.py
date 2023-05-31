import sys
import os
import stat

def change_permissions(mode, *files):
    for fname in files:
        if os.path.isfile(fname):
            os.chmod(fname, mode)
            print(f"Changed permissions of {fname} to {oct(mode)}")
        else:
            print(f"{fname} does not exist.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py mode file1 file2 ...")
        sys.exit(1)

    mode = int(sys.argv[1], 8) # assuming mode is provided in octal
    files = sys.argv[2:]
    change_permissions(mode, *files)
