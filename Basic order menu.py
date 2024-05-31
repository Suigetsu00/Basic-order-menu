fruits = ["Apple", "Orange", "Mango"]
vegetables = ["Tomato", "Celery", "Broccoli"]
meat = ["Chicken", "Pork", "Beef"]

print("Type 1 for fruits")
print("Type 2 for vegetables")
print("Type 3 for meat")
print("Type 0 to exit")

while True:
    menu = int(input("Type the menu number: "))
    menu = int(menu)
    if menu == 1:
        print(fruits)
        break
    elif menu == 2:
        print(vegetables)
        break
    elif menu == 3:
        print(meat)
        break
    elif menu == 0:
        print("Exiting...")
        break
    else:
        print("Invalid Number, not on the menu!")
