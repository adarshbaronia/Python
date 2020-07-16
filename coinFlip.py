import random

print("Welcome to the coin flip App")
print()
print("I will flip the coin a set number of times.")
#get the user Input
flip_number = int(input("How many times would you like me to flip the coin:  "))
choice = input("Would you like to see the result of each flip (y/n): ").lower()

print("\nFlipping!!!!\n")
#initalzing variables
heads = 0
tails = 0

#main loop
for flips in range(flip_number):
  #create the coin object
    coin = random.randint(0, 1)

    if coin == 1:
      heads += 1
      if choice.startswith('y'):
        print('Heads')
    else:
      tails += 1
      if choice.startswith('y'):
        print('Tails')

    if heads == tails:
      print(f"At {flips + 1} flips, number of heads and tails were equal {heads} each")

#calculating percantages of each flip
heads_percentage = round(100 * heads / flip_number, 2)
tails_percentage = round(100 * tails / flip_number, 2)

# results
print("\nResults of flipping a coin " + str(flip_number) +"times: ")
print("\nSide\t\tCount\t\tPercantages")
print("Heads\t\t "+ str(heads) + "/" + str(flip_number) + "\t\t" + str(heads_percentage) + "%")
print("Tails\t\t "+ str(tails) + "/" + str(flip_number) + "\t\t" + str(tails_percentage) + "%")






