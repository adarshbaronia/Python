def get_info():
    """ get user info to store in a dict that represent a bak account"""
    name = input("Hello, Please enter your name: ").title().strip()
    savings = int(
        input("How much money would you like to set up your saving account with: "))
    checking = int(
        input("How much money would you like to set up your checking in account with: "))

    bank_account = {
        "Name": name,
        "Savings": savings,
        "Checking": checking,
    }
    return bank_account


def make_deposit(bank_account, account, money):
    """ Add monsy to specific type of account"""
    bank_account[account] += money
    print("\nDeposited $" + str(money) + " into " +
          bank_account['Name'] + " 's " + account.lower())


def make_withdrawal(bank_account, account, money):
    """ withdraw money from a specific type of account"""
    if bank_account[account] - money >= 0:
        bank_account[account] -= money
        print(
            f"\n Withdrew $ {str(money)} from {bank_account['Name']}'s account".lower())
    # not enough money to withdraw
    else:
        print(
            f"\nSorry, by withdrawing ${money}, you will have a negative balance!")


def display_info(bank_account):
    """Display all key-value pairs in a given bank account"""
    print("\nCurrent Account Information")
    for key, value in bank_account.items():
        if key == 'Name':
            print(key + ":  " + str(value))
        else:
            print(key + ": $ " + str(value))


# main code
# create a bank account
my_account = get_info()
running = True
while running:
    display_info(my_account)
    # get user info for the transcation
    account_type = input(
        "\nWhat account would you like to access (Savings or Checking): ").title()
    choice = input(
        "What type of transcation would you like to make (Deposite or Withdrawal): ").title()
    amount = float(input("Please enter the amount: "))
    # call the function based on user input
    if account_type == "Savings" or account_type == "Checking":
        if choice == "Deposite":
            make_deposit(my_account, account_type, amount)
        elif choice == "Withdrawal":
            make_withdrawal(my_account, account_type, amount)
        else:
            print("\nSorry, We can not do that for you today!")
    else:
        print("\nSorry, We can not do that for you today!")

    choice = input("Would you like to make anothr transcation (y/n):")
    if choice != 'y':
        display_info(my_account)
        print("\nThank you. have a great day!")
        running = False
