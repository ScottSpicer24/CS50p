def main():
    fuel = input("What fraction is your gas tank at:")
    percent = convert(fuel)
    level = gauge(percent)
    print(level)


def convert(fraction):
    try:
        x,y = fraction.split("/")
    except ValueError:
        main()
        quit()

    if x.isnumeric() == False:
        main()
        quit()
    
    if y.isnumeric() == False:
        main()
        quit()
    
    x = int(x)
    y = int(y)

    if x > y:
        main()
        quit()
    
    try:
        percent = (x/y) * 100
        return round(percent)
    except ZeroDivisionError:
        main()
        quit()


def gauge(percent):
    if int(percent) >= 99:
        return 'F'
    elif int(percent) <= 1:
        return "E"
    else:
        return f"{percent}%"


if __name__ == "__main__":
    main()