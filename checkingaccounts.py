import csv
import sys
import logging
import os
import pwd

def read_csv(csv_file):
    try:
        with open(csv_file, "r") as csvfile:
            csvreader = csv.DictReader(csvfile)
            print(next(csvreader))
            return list(csvreader)
    except IOError as e:
        logging.error(f"Failed to open CSV file: {str(e)}")
        sys.exit(1)

def user_exists(username):
    try:
        pwd.getpwnam(username)
        return True
    except KeyError:
        return False

def create_user(username, password):
    os.system(f"useradd {username}")
    os.system(f"echo {username}:{password} | chpasswd")
    logging.info(f"User {username} created.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py /path/to/csvfile")
        sys.exit(1)

    logging.basicConfig(level=logging.INFO)

    csv_file = sys.argv[1]
    users = read_csv(csv_file)

    for user in users:
        print(user['password'])
        if user_exists(user['account']):
            logging.info(f"User {user['account']} already exists.")
        else:
            create_user(user['account'], user['password'])
