# Printing the welcome message
print("Welcome to the voter Registration App")
print()
# asking for input
name = input("Please enter your name: ").title()
age = int(input("Please enter your age: "))
print()
parties = ["Republican", "National congress",
           "BJP", "Independent", "Libertarian", "Labour"]
print()
# if conditin for user about his age
if age >= 18:
    print(f"\nCongratulations {name}! you are old enough to register")
    print("\nHere is the list of political parties to join.")

    for party in parties:
        print(f"\t- {party}")
    # user input to choose party
    chosen_party = input("\nWhat party would like to join: ").title().strip()

    # print a message for each party
    if chosen_party in parties:
        print(
            f"\nCongratulations {name}! You have joined the {chosen_party} party.")
        if chosen_party == 'Republican' or chosen_party == 'National congress' or chosen_party == 'BJP':
            print("That is a major party")
        elif chosen_party == 'Independent':
            print("You are an Indepedent person!")
        elif chosen_party == 'Libertarian':
            print("You took a wrong turn.")
        else:
            print("That is not a major party.")
    else:
        print("Wrong Selection!!!")
# if user is not 18
else:
    print("You aren't old enough to vote!")
