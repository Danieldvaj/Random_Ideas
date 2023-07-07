import os
import grp
import pwd

def create_file_if_not_exists(filename):
    """Create a file if it does not exist."""
    if not os.path.exists(filename):
        open(filename, 'a').close()

def set_owner_and_group(filename, owner, group):
    """Set the owner and group of a file."""
    try:
        uid = pwd.getpwnam(owner).pw_uid
        gid = grp.getgrnam(group).gr_gid
        os.chown(filename, uid, gid)
        print(f"Changed ownership of {filename} to {owner}:{group}")
    except Exception as e:
        print(f"Failed to change owner or group for {filename}: {e}")

def manage_file(filename, owner, group):
    """Create a file (if it does not exist) and set its owner and group."""
    create_file_if_not_exists(filename)
    set_owner_and_group(filename, owner, group)

# List of files and their desired properties
files_and_properties = [
    {"filename": "file1", "owner": "root", "group": "root"},
    {"filename": "file2", "owner": "root", "group": "othergroup"},
    {"filename": "file3", "owner": "otheruser", "group": "othergroup"},
]

# Apply properties to each file
for file_properties in files_and_properties:
    manage_file(**file_properties)
