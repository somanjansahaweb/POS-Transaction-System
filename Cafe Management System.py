Menu = { 
    "Pizza": 50.00, 
    "Burger": 30.00, 
    "Pasta": 40.00, 
    "Salad": 50.00, 
    "Coffee": 40.00
} 
print("Welcome to Our Restaurant") 
print("Here is the Menu:") 
for key, value in Menu.items():
    print(f"{key}: Rs {value}")   
order_total = 0

item_1 = input("Enter the item you want to order: ") 
if item_1 in Menu: 
    order_total += Menu[item_1]
    print(f"{item_1} added to your menu cart")   
else: 
    print(f"{item_1} is not available") 
another_order = input("Do you want to order another item? (yes/no): ") 
if another_order.lower() == "yes": 
    item_2 = input("Enter the second item you want to order: ") 
    if item_2 in Menu: 
        order_total += Menu[item_2]
        print(f"{item_2} added to your menu cart")   
    else: 
        print(f"{item_2} is not available") 
another_order = input("Do you want to order another item? (yes/no): ") 
if another_order.lower() == "yes": 
    item_3 = input("Enter the third item you want to order: ") 
    if item_3 in Menu: 
        order_total += Menu[item_3]
        print(f"{item_3} added to your menu cart") 
    else:
        print(f"{item_3} is not available")
another_order = input("Do you want to order another item? (yes/no): ") 
if another_order.lower() == "yes": 
    item_4 = input("Enter the fourth item you want to order: ") 
    if item_4 in Menu: 
        order_total += Menu[item_4]
        print(f"{item_4} added to your menu cart") 
    else:
        print(f"{item_4} is not available")
another_order = input("Do you want to order another item? (yes/no): ") 
if another_order.lower() == "yes": 
    item_5 = input("Enter the fifth item you want to order: ") 
    if item_5 in Menu: 
        order_total += Menu[item_5]
        print(f"{item_5} added to your menu cart") 
    else: 
        print(f"{item_5} is not available")
print(f"Your total order amount is: Rs {order_total}") 
print("Thank you for dining with us!") 
print("We hope to see you again soon!")

