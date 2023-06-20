'''
In a file called working.py, implement a function called convert that expects a str in either of the 12-hour formats below
and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein)
and that there will be a space before each. Assume that these times are representative of actual times,
not necessarily 9:00 AM and 5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM
Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid
(e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone's hours will start ante meridiem and end post meridiem;
someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

Structure working.py as follows, wherein you're welcome to modify main and/or implement other functions as you see fit,
but you may not import any other libraries. You're welcome, but not required, to use re and/or sys.
'''
import re


def main():
    print(convert(input("Hours: ")))


def convert(time):
    time = time.strip()
    if re.search(r'^\d(\d)?:\d\d (A|P)M to \d(\d)?:\d\d (A|P)M$', time):
        before = re.search(r'^(.+):(.+) (.+)M to (.+):(.+) (.+)M$', time)
        hour_1 = int(before.group(1))
        if hour_1 > 12:
            return ValueError 
        min_1 = before.group(2)
        hour_2 = int(before.group(4))
        if hour_2 > 12:
            return ValueError 
        min_2 = before.group(5)
        if min_1 > '59' or min_2 > '59':
            return ValueError
        if before.group(3) == "P" and hour_1 != 12:
            hour_1 += 12
        if before.group(6) == "P" and hour_2 != 12:
            hour_2 += 12
        if before.group(3) == "A"and hour_1 == 12:
            hour_1 = '00'
        if before.group(6) == "A" and hour_2 == 12:
            hour_2 = '00'
        return f"{hour_1}:{min_1} to {hour_2}:{min_2}"
    elif re.search(r'^\d(\d)? (A|P)M to \d(\d)? (A|P)M$', time):
        before = re.search(r'^(.+) (.+)M to (.+) (.+)M$', time)
        hour_1 = int(before.group(1))
        if hour_1 > 12:
            return ValueError 
        hour_2 = int(before.group(3))
        if hour_2 > 12:
            return ValueError 
        if before.group(2) == "P" and hour_1 != 12:
            hour_1 += 12
        if before.group(4) == "P" and hour_2 != 12:
            hour_2 += 12
        if before.group(2) == "A" and hour_1 == 12:
            hour_1 = '00'
        if before.group(4) == "A" and hour_2 == 12:
            hour_2 = '00'        
        return f"{hour_1} to {hour_2}"
    else:
        return ValueError


if __name__ == "__main__":
    main()