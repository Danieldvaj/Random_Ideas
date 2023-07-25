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

def check_permissions(filename, perms):
    if oct(os.stat(filename).st_mode)[-3:] != str(perms):
        os.chmod(filename, perms)
        print(f"Changed permissions of {filename} to {perms}")

def manage_file(filename, user, group, perms):
    create_file(filename)
    check_owners(filename, user, group)
    check_permissions(filename, perms)

if __name__ == "__main__":
    files = [
        {"filename": "group_only.txt", "user" : "root", "group": "wheel", "perms" : 0o660},
        {"filename": "public_knowledge.txt", "user" : "root", "group": "root", "perms" : 0o644},
        {"filename": "secret.txt", "user" : "root", "group": "root", "perms" : 0o600},
        {"filename": "secret.txt.pgp", "user" : "root", "group": "root", "perms" : 0o644},
        {"filename": "wiki.txt", "user" : "nobody", "group": "nogroup", "perms" : 0o777}
    ]
    for file in files:
        manage_file(**file)

