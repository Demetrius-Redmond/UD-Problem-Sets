menu = {"Burger": 9.50, "Vegan Burger": 11.00, "Hot Dog": 5.00, "Cheese Dog": 7.00, "Fries": 5.00, "Cheese Fries": 6.00, "Cold Pressed Juice": 7.00, "Cold Brew": 3.00, "Water": 2.00, "Soda": 2.00}

total = 0

while True:
    order = input("Enter a food item: ").title()
    if order in menu:
        total += (menu.get(order))  
    elif order == "":
        break       
    else: 
        print(f'"{order}" is not a valid option')
        continue
print(f"Your total cost is: ${format(total, '.2f')}")

# I had to google the format method