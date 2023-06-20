'''
implement a program that prompts the user for a date, anno Domini, in month-day-year order, 
formatted like 9/8/1636 or September 8, 1636, Then output that same date in YYYY-MM-DD format. 
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
    date_initial = date_initial.strip()
    date_seperated = date_initial.split("/")
    if len(date_seperated) == 1:
        date_seperated = date_initial.split()
        if len(date_seperated) != 3:
            main()
            return 0
        date_seperated[0] = date_seperated[0].title().strip()
        date_seperated[1] = date_seperated[1].strip()
        date_seperated[2] = date_seperated[2].strip()
        date_seperated[1] = date_seperated[1].replace(',', '')
        flag = 0
        for i in range(0, 9):
            if date_seperated[0] == months[i]:
                date_seperated[0] = '0' + str(i+1)
                flag = 1
            else:
                continue
        for i in range(9, 12):
            if date_seperated[0] == months[i]:
                date_seperated[0] = i+1
                flag = 2
        if flag == 0:
            main()
            return 0
    elif len(date_seperated) != 3:
        main()
        return 0
    else:
        date_seperated[0] = date_seperated[0].strip()
        date_seperated[1] = date_seperated[1].strip()
        date_seperated[2] = date_seperated[2].strip()
        try:
            if int(date_seperated[0]) > 12 or int(date_seperated[0]) < 1:
                main()
                return 0
            elif int(date_seperated[0]) > 0 and int(date_seperated[0]) < 10:
                date_seperated[0] = '0' + str(date_seperated[0])
        except ValueError:
            main()
            return 0
    try:   
        if int(date_seperated[1]) > 31 or int(date_seperated[1]) < 1:
            main()
            return 0
        elif int(date_seperated[1]) > 0 and int(date_seperated[1]) < 10:
            date_seperated[1] = '0' + str(date_seperated[1])
    except ValueError:
        main()
        return 0

    print(f"{date_seperated[2]}-{date_seperated[0]}-{date_seperated[1]}")

main()
