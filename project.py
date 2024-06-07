menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Sandwich': 65,
    'Tea': 20,
    'Coffee': 30,
}

print("Welcome to Ashu's restaurant")
print("Pizza: Rs40\nPasta: Rs50\nSandwich: Rs65\nTea: Rs20\nCoffee: Rs30")

order_total = 0

item_1 = input("Enter the name of item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item? (Yes/No) ")
if another_order.lower() == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} is not available!")

print(f"The total amount to pay is Rs{order_total}")
