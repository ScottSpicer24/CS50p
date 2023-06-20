'''
In a file called seasons.py, implement a program that prompts the user for their date of birth in YYYY-MM-DD format 
and then sings prints how old they are in minutes, rounded to the nearest integer.
Since a user might not know the time at which they were born, assume, for simplicity, 
that the user was born at midnight (i.e., 00:00:00) on that date. And assume that the current time is also midnight. 
In other words, even if the user runs the program at noon, assume that it's actually midnight, on the same date. 
Use datetime.date.today to get today's date, per docs.python.org/3/library/datetime.html#datetime.date.today.
'''

from datetime import date

class Age:
    def __init__(self, bday, age):
        self.bday = bday
        self.age = age

    def __str__(self):
        return f"you are {str(self.age)} minutes old"
    
    @classmethod
    def get(cls):
        bday = input("input your birthday in YYYY-MM-DD: " )
        year1, month1, day1 = bday.strip().split('-')
        year1 = int(year1)
        month1 = int(month1)
        day1 = int(day1)
        day = str(date.today())
        year2, month2, day2 = day.strip().split('-')
        year2 = int(year2)
        month2 = int(month2)
        day2 = int(day2)
        if month2 > month1:
            y_diff = (year2 - year1) * 365 * 24 * 60
            m_diff = (month2 - month1) * 30.4 * 24 * 60
            d_diff = day2 * 24 * 60
            age = y_diff + m_diff + d_diff
        elif month2 == month1:
            if day2 > day1:
                y_diff = (year2 - year1 - 1) * 365 * 24 * 60
                m_diff = (month2 - 1) * 30.4 * 24 * 60
                d_diff = day2 * 24 * 60
                age = y_diff + m_diff + d_diff
            elif day2 < day1:
                y_diff = (year2 - year1) * 365 * 24 * 60
                d_diff = (day1 - day2) * 24 * 60
                age = y_diff + d_diff
            else:
                age = (year2 - year1) * 365 * 24 * 60 
        else:
            y_diff = (year2 - year1 - 1) * 365 * 24 * 60
            m_diff = month2 * 30.4 * 24 * 60
            d_diff = day2 * 24 * 60
            age = y_diff + m_diff + d_diff  
        '''
        leapyears = 0
        while year2 >= year1:
            if (year2 % 4 == 0 and year2 % 100 != 0) or (year2 % 400 == 0):
                leapyears += 1
                year2 -= 1
            else:
                year2 -= 1
        age += leapyears * 24 * 60
        '''
        return cls(bday, age)


def main():
    person = Age.get()
    print(person)


if __name__ == "__main__":
    main()