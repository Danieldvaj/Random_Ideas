import os
import sys
import grp
import pwd

def create_file(filename):
    if not os.path.isfile(filename):
        open(filename, "a").close()

def check_owners(filename, user, group):
    stat_info = os.stat(filename)
    current_user = pwd.getpwuid(stat_info.st_uid).pw_name
    current_group = grp.getgrgid(stat_info.st_gid).gr_name
    
    try:
        if current_user != user:
            uid = pwd.getpwnam(user).pw_uid
            os.chown(filename, uid, -1)  # -1 keeps group the same
            print(f"Changed user of {filename} to {user}")

        if current_group != group:
            gid = grp.getgrnam(group).gr_gid
            os.chown(filename, -1, gid)  # -1 keeps user the same
            print(f"Changed group of {filename} to {group}")
    except KeyError as e:
        print(f"User or group not found: {e}")
    except OSError as e:
        print(f"Failed to change owner or group for {filename}: {e}")

def manage_file(filename, user, group):
    create_file(filename)
    check_owners(filename, user, group)


if __name__ == "__main__":
    files = [{"filename": "ferrari1.txt", "user" : "root", "group": "root"},
             {"filename": "ferrari2.txt", "user" : "wheel", "group": "root"},
             {"filename": "ferrari3.txt", "user" : "root", "group": "kali"}]
    for file in files:
        manage_file(**file)
