import os
import sys

def create_symlink(target, link_name):
    try:
        os.symlink(target, link_name)
        print(f"Symlink created from {link_name} to {target}.")
    except OSError as e:
        print(f"Failed to create symlink: {str(e)}")

def remove_symlink(link_name):
    try:
        os.remove(link_name)
        print(f"Symlink {link_name} removed.")
    except OSError as e:
        print(f"Failed to remove symlink: {str(e)}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 script.py <operation> <target_path> [<link_path>]")
        return

    operation = sys.argv[1]
    target = sys.argv[2]

    if operation == "create":
        if len(sys.argv) != 4:
            print("Error: Link path is required for symlink creation.")
            return
        link_name = sys.argv[3]
        create_symlink(target, link_name)
    elif operation == "remove":
        remove_symlink(target)
    else:
        print(f"Error: Unknown operation {operation}.")

if __name__ == "__main__":
    main()
