print("Welcome to the yes or No Issue Polling App ")
# get user input
issue = input("What is the yes or no issue you will be voting on today: ")
print()
vote_number = int(
    input("What is the number of voters you allow on the issue: "))
password = input("Please enter a password: ")
print()
yes = 0
no = 0
results = {}
for i in range(vote_number):
    name = input("Enter your full name: ").title().strip()
    if name in results.keys():
        print("Sorry, it seems that someone with that name has already voted. ")
    else:
        print(f"Here is the today's issue: {issue}")
        choice = input("What do you think..yes or no: ").lower().strip()
        print()
        if choice == 'yes' or choice == 'y':
            choice = 'yes'
            yes += 1
        elif choice == 'no' or choice == 'n':
            choice = 'no'
            no += 1
        else:
            print("That is not a yes or no answer, but okay...")
            print()
        # add votes to dict results
        results[name] = choice
        print(
            f"Thank you! {name} your vote of {results[name]} has been registered.")
        print()
# showing the summery
total_votes = len(results.keys())
print("\nThe following " + str(total_votes) + " people voted: ")
for key in results.keys():
    print(key)


print("\n On the followng issue: " + issue)
if yes > no:
    print(f"Yes wins! {yes} yes votes to {no} no.")
elif no > yes:
    print(f"No wins! {no} noes votes to {yes} yes.")
else:
    print(f"It was a tie! {no} noes votes to {yes} yes. ")

guess = input("\nTo see the voting results enter password: ")
if guess == password:
    for key, value in results.items():
        print(f"Voter: {key} \t\t Vote: {value}")
else:
    print("Sorry, Incorrect password. Goodbye")

print("\nThank you for using th issue polling app.")
