'''
in a file called lines.py, implement a program that expects exactly one command-line argument, the name (or path) of a Python file,
and outputs the number of lines of code in that file, excluding comments and blank lines.
If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py,
or if the specified file does not exist, the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, is a comment.
(A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.
'''

import sys

# make sure only 1 command line argument
if len(sys.argv) != 2:
    sys.exit

# make sure file if a python file
try:
    file_name, file_type = sys.argv[1].split('.')
    file_type = file_type.lower().strip()
    if file_type != 'py':
        sys.exit
except ValueError:
    sys.exit

# OPEN file
# line that starts with '#' is a comment
# blank lines do not count
lines = 0
try:
    with open(sys.argv[1], 'r') as file:
        for line in file:
            if len(line.strip()) == 0:
                continue
            elif line.lstrip().startswith('#'):
                continue
            else:
                lines += 1
except FileNotFoundError:
    sys.exit()

print(lines)