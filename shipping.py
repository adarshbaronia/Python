#a list of users
users = ['sid', 'Bob', 'Jhon', 'davis', 'allen']

print("Welcome to the Shipping Accounts Department")
print()
# ask for input
name = input("Hello, What is your username: ").lower().strip()
if name in users:
    #showing charges
    print()
    print(f"Hello {name}, Welcome back to your account.")
    print("Curent shipping charges are as follows:")
    print()
    print("Shipping orders 0 to 100:\t\t $5.10 each")
    price1 = 5.10
    print("Shipping orders 100 to 500:\t\t $5.00 each")
    price2 = 5.00
    print("Shipping orders 500 to 1000:\t\t $4.95 each")
    price3 = 4.95
    print("Shipping orders over 1000:\t\t $5.80 each")
    price4 = 4.80
    print()

    # asked for number of items for shipping
    items = int(input("How many items would you like to ship: "))
    if items > 0 & items < 100:
        cost = items * price1
        print(f"To ship {items} items it will cost you {round(cost,2)} at ${price1} per item.")
    elif items > 100 & items < 500:
        cost = items * price2
        print(f"To ship {items} items it will cost you {round(cost,2)} at ${price2} per item.")
    elif  items > 500 & items < 1000:
        cost = items * price3
        print(f"To ship {items} items it will cost you {round(cost,2)} at ${price3} per item.")
    elif items > 0 & items < 100:
        cost = items * price4
        print(f"To ship {items} items it will cost you {round(cost,2)} at ${price4} per item.")

    #ask to place the order
    print()
    order = input("Would you like to place this order (y/n): ").lower()
    if order.startswith('y'):
        print(f"Your Order has been placed. items: {items} And cost: {round(cost, 2)} Thank you!")
    else:
        print("Okay, No order is being placed at this time. Thank you!")    
else:
    print(f"Sorry, {name}! you yet to open an account with us. Thank you ")