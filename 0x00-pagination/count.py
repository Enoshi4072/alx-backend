import subprocess

def count_lines(filename):
    result = subprocess.run(['wc', '-l', filename], stdout=subprocess.PIPE)
    line_count = int(result.stdout.split()[0])
    return line_count

filename = 'Popular_Baby_Names.csv'
num_lines = count_lines(filename)
print("Number of lines in the file:", num_lines)
