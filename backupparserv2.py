import os
import glob
from datetime import datetime

# Glob pattern to match all backup files
pattern = "backup_*.tar.gz"

# Get a list of all matching files
files = glob.glob(pattern)

# If there are more than one backup files, proceed to delete the old ones
if len(files) > 1:
    # Sort files based on the date in their filename
    files.sort(key=lambda x: datetime.strptime(x, 'backup_%Y%m%d.tar.gz'))

    # Keep the most recent file, delete the rest
    for file in files[:-1]:  # This excludes the last item in the list
        os.remove(file)
        print(f"Deleted file: {file}")
