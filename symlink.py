import sys
import os


def get_symlinkfile(src):
    for root, dirs, files in os.walk("."):
        if src in files:
            return os.path.join(root, src)


def check_symlink(dst):
    return os.path.islink(dst)


def unlink_sym(dst):
    try:
        os.unlink(dst)
    except OSError as e:
        print(f"Unlinking failed with the error: {e}")
        sys.exit(1)


def symlink_file(src, dst):
    file = get_symlinkfile(src)
    if file is not None:
        try:
            os.symlink(file, dst)
            print("Symlink successfully created")
        except OSError as e:
            print(f"Symlinking failed {e}")
            sys.exit(1)
    else:
        print(f"Source file {src} not found")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py /name/to/path")
        sys.exit(1)

    src = sys.argv[1]
    if "prod" not in src and "test" not in src:
        print("Incorrect database symlink file")
        sys.exit(1)
    dst = sys.argv[2]
    if not os.path.isfile(dst):
        print("Incorrect destination file")
        sys.exit(1)

    if check_symlink(dst):
        unlink_sym(dst)

    symlink_file(src, dst)
