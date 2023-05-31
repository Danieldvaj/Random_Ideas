import sys
import os
import zipfile

def compress_files(directory, extension, output_filename):
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(extension):
                    zipf.write(os.path.join(root, file))
    print(f"Compressed files into: {output_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py directory extension output_filename")
        sys.exit(1)

    directory = sys.argv[1]
    extension = sys.argv[2]
    output_filename = sys.argv[3]
    compress_files(directory, extension, output_filename)
