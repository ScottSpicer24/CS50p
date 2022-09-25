
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

try:
    while True:
        order = input("What would you like to eat: ")
        order = order.title().strip()
        print(order)
        try:
            total += menu[order]
            print(f"${total}")
        except KeyError:
            pass
except EOFError:
    print("end of order")