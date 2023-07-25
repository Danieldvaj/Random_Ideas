import re

def read_data(filename):
    with open(filename, "r") as file_data:
        data = file_data.readlines()
        print("Parsing processlist.txt")
        return data

def count_processes(data):
    process_data = [line for line in data if not "PID COMMAND" in line]
    print(f"Total number of processes: {len(process_data)}")

def user_invoked(data):
    count = 0
    for line in data:
        # Assuming that user-invoked processes are those indented 5 spaces or more
        print(len(line), "eerste", line)
        print(len(re.sub(r'(\d+)\s+(\\_)', r'\1\2', line)), "tweede" , re.sub(r'(\d+)\s+(\\_)', r'\1\2', line) )
        if len(line) - len(re.sub(r'(\d+)\s+(\\_)', r'\1\2', line)) >= 5:
            count += 1
    print(f"User processes{count}")

def count_scripts(data):
    scripts = {}
    for line in data:
        # Find the script names
        match = re.search(r'(\./\w+\.sh)', line)
        if match:
            script = match.group()
            # Count the occurrences of each script
            scripts[script] = scripts.get(script, 0) + 1

    print("Active scripts")
    for script, count in scripts.items():
        print(f"    {count}x {script}")

if __name__ == "__main__":
    data = read_data('process-list.txt')
    count_processes(data)
    user_invoked(data)
    count_scripts(data)
