'''
In a file called response.py, using either validator-collection or validators from PyPI, 
implement a program that prompts the user for an email address via input and then prints Valid or Invalid, respectively, 
if the input is a syntatically valid email address. 

YOU MAY NOT USE re. 
do not validate whether the email address's domain name actually exists
'''

import validator_collection

def main():
    print(valid(input("Email: ")))

def valid(email):
    try:
        validator_collection.email(email)
        return "Valid"
    except ValueError:
        return "Invalid"

main()