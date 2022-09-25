# turn a fraction into a precent.

# check for non numbers
# check for div by 0
# check for x > y

def main():
    
    fuel = input("What fraction is your gas tank at:")

    try:
        x,y = fuel.split("/")
    except ValueError:
        main()
        return 0

    if x.isnumeric() == False:
        main()
        return 0 
    
    if y.isnumeric() == False:
        main()
        return 0 
    
    x = int(x)
    y = int(y)

    if x > y:
        main()
        return 0
    
    try:
        percent = (x/y) * 100
        if percent >= 99:
            print("F")
        elif percent <= 1:
            print("E")
        else:
            print(f"{round(percent)}%")
    except ZeroDivisionError:
        main()
        return 0

if __name__ == "__main__":
    main()