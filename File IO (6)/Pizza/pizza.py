'''
In a file called pizza.py, implement a program that expects exactly one command-line argument, 
the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate, 
a package on PyPI at pypi.org/project/tabulate. Format the table using the library’s grid format. 
If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv, 
or if the specified file does not exist, the program should instead exit via sys.exit.
'''
import sys
import csv
from tabulate import tabulate

if len(sys.argv) != 2:
    sys.exit()

try:
    file_name, file_type = sys.argv[1].split('.')
    file_type = file_type.lower().strip()
    if file_type != 'csv':
        sys.exit()
except IndexError:
    sys.exit()

pizza = []
try:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for row in reader:
            pizza.append({"type": row[0], "small": row[1], "large" :row[2]})
except IndexError:
    sys.exit()
except FileNotFoundError:
    sys.exit()

print(tabulate(pizza, headers='firstrow', tablefmt='grid'))