'''
In a file called numb3rs.py, implement a function called validate that expects an IPv4 address as input as a str 
then returns True or False, respectively, if that input is a valid IPv4 address or not.

Structure numb3rs.py as follows, wherein you're welcome to modify main and/or implement other functions as you see fit, 
but you may not import any other libraries. You're welcome, but not required, to use re and/or sys.

An IPv4 address is a numeric identifier formatted as #.#.#.#. But each # should be a number between 0 and 255, inclusive.
'''
import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\.$", ip.strip()):
        ip_nums = ip.split('.')
        for i in range(0,4):
            if int(ip_nums[i]) >= 0 and int(ip_nums[i]) <= 255:
                continue
            else:
                return False
        return True
    else:
        return False
    

if __name__ == "__main__":
    main()
