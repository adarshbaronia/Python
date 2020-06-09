print("Welcome to the Factor Generator App")
print()
running = True
# running the program untill user quits
while running:
    number = int(
        input("\nEnter a number to determine all factors of that number: "))
    # find the factors of the user input
    factors = []
    for i in range(1, number+1):
        if number % i == 0:
            factors.append(i)

    # print the factors
    print("\nFactors of " + str(number) + " are: ")
    for factor in factors:
        print(factor)
    # print a summery of factors
    print("\nIn summery: ")
    for i in range(int(len(factors)/2)):
        print(f"{str(factors[i])} *  {str(factors[-i-1])} = {str(number)}")

    choice = input("\nRun again (y/n): ").lower()
    if choice != 'y':
        running = False
        print("Thank you!")
