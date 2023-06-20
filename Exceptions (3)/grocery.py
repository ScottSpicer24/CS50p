'''
implement a program that prompts the user for items, one per line, until the user inputs control-d 
(which is a common way of ending one’s input to a program). 
Then output the user’s grocery list in all uppercase, sorted alphabetically by item, 
prefixing each line with the number of times the user inputted that item. No need to pluralize the items. 
Treat the user’s input case-insensitively.
'''


grocery = {}
try:
    while True:
        item = input("")
        item = item.upper()
        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1
except EOFError:
    grocery_sorted = sorted(grocery.keys())
    for i in range(0, len(grocery)):
        print(f"{grocery[grocery_sorted[i]]} {grocery_sorted[i]}")