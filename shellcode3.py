import sys
import os

def combine_files(output_file, *input_files):
    with open(output_file, 'w') as outfile:
        for fname in input_files:
            if os.path.isfile(fname):
                with open(fname) as infile:
                    for line in infile:
                        outfile.write(line)
            else:
                print(f"{fname} does not exist.")
                
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py output_file input_file1 input_file2 ...")
        sys.exit(1)

    output_file = sys.argv[1]
    input_files = sys.argv[2:]
    combine_files(output_file, *input_files)
