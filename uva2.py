import re

def extract_ips(input_files, output_file):
    # Regular expression pattern for IPv4 addresses
    ip_pattern = re.compile(
        r'\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.)){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b')

    with open(output_file, 'w') as outfile:
        for input_file in input_files:
            with open(input_file, 'r') as infile:
                for line in infile:
                    matches = re.findall(ip_pattern, line)
                    for match in matches:
                        # Each match is a tuple, where the full match is the first element
                        outfile.write(match[0] + '\n')

# List of input files
input_files = ['input1.txt', 'input2.txt', 'input3.txt']
output_file = 'output.txt'

extract_ips(input_files, output_file)
