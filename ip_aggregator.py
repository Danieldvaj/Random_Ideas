import os
import re
import sys

def extract_ip(filename):
    # This regular expression matches any IP address
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    try:
        ip = re.findall(ip_pattern, filename)
    except TypeError:
        print(f"Filename is not a string: {filename}")
        sys.exit(1)
    return ip

def copy_files_with_ip(directory, target_directory):
    # Check if the target directory exists and is writable
    if not os.path.isdir(target_directory) or not os.access(target_directory, os.W_OK):
        print(f"Target directory does not exist or is not writable: {target_directory}")
        sys.exit(1)

    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            ip_addresses = extract_ip(filename)
            if ip_addresses:
                source_file = os.path.join(dirpath, filename)
                for ip in ip_addresses:
                    target_file = os.path.join(target_directory, ip + ".txt")
                    try:
                        with open(source_file, 'r') as f_src, open(target_file, 'a') as f_tgt:
                            f_tgt.write(f_src.read())
                        print(f"Appended content of {source_file} to {target_file}")
                    except IOError as e:
                        print(f"Failed to copy content from {source_file} to {target_file}: {str(e)}")
                        sys.exit(1)

directory = "."
target_directory = "."
copy_files_with_ip(directory, target_directory)
