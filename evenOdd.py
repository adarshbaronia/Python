print("Welcome to the Even Odd Number Sorter App: ")
print()
running = True
while running:
    num_string = input(
        "Enter in a string of numbers seperated by a comma (,) : ")
    num_string = num_string.replace('', '')
    num_list = num_string.split(',')

    # Initalize lists to hold even and odd numbers
    evens = []
    odds = []

    # finding even and odd
    for number in num_list:
        number = int(number)
        if number % 2 == 0:
            evens.append(number)
            print(f"\t{str(number)}  is even!")
        else:
            odds.append(number)
            print(f"\t{str(number)} is odd!")
    # sort the lists even and odds
    evens.sort()
    odds.sort()

    # showing the numbrs
    print(f"\nThe following {str(len(evens))} numbers are even: ")
    for even in evens:
        print("\t" + str(even))

    print(f"\nThe following {str(len(odds))} numbers are odd: ")
    for odd in odds:
        print("\t" + str(odd))

    # asking user for input to continue
    choice = input("\nWould you like to run the progrm again (y/n): ").lower()
    if choice != 'y':
        running = False
        print("Thank you!!!")
