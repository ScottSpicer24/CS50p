'''
in a file called scourgify.py, implement a program that:

Expects the user to provide two command-line arguments:
the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
Converts that input to that output, splitting each name into a first name and last name. 
Assume that each student will have both a first name and last name.
If the user does not provide exactly two command-line arguments, or if the first cannot be read, 
the program should exit via sys.exit with an error message.
'''
import sys
import csv

# check for correct number of files
def main():
    if len(sys.argv) != 3:
        sys.exit()
    # check that they are csv files
    file1_name, file1_type = sys.argv[1].split('.')
    file2_name, file2_type = sys.argv[2].split('.')
    if file1_type.strip() != 'csv' or file2_type.strip() != 'csv':
        sys.exit()
    name = []
    house = []
    # open file, ecxept finle not found
    with open(sys.argv[1]) as file1:
        reader = csv.reader(file1)
        for row in reader:
            # read in to a list
            name.append(row[0])
            house.append(row[1])
    print(name)
    print(house)

    # split name in 2
    first = []
    last = []
    for i in range(1, len(name)):
        name2, name1 = name[i].split(',')
        first.append(name1.strip())
        last.append(name2.strip())
    print(first)
    print(last)
    # open 2nd file
    with open(sys.argv[2], 'a') as file2:
        writer = csv.writer(file2)
        # write new names in file
        for i in range(0, len(first)):
            writer.writerow([first[i],last[i],house[i+1]])
    
main()