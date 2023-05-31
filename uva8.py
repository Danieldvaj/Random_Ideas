import sys
import os
from collections import Counter
import re

def count_words(*files):
    word_counter = Counter()
    for fname in files:
        if os.path.isfile(fname):
            with open(fname) as f:
                content = f.read().lower()
                words = re.findall(r'\b\w+\b', content)
                word_counter.update(words)
    
    for word, count in word_counter.most_common(10):
        print(f"{word}: {count}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py file1 file2 ...")
        sys.exit(1)

    files = sys.argv[1:]
    count_words(*files)
