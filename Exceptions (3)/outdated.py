'''
implement a program that prompts the user for a date, anno Domini, in month-day-year order, 
formatted like 9/8/1636 or September 8, 1636
'''

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    date_initial = input("date: ")

    try:
        date_seperated = date_initial.split("/")
        if int(date_seperated[0]) > 12 or int(date_seperated[0]) < 1:
            main()
            return 0
    except ValueError:
        date_seperated = date_initial.split()
        date_seperated[0] = date_seperated[0].title()
        if date_seperated[0] not in months:
            main()
            return 0

    if int(date_seperated[1]) > 31 or int(date_seperated[1]) < 1:
        main()
        return 0

    print(date_seperated)

main()
