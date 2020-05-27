import random

print("Welcome to the Number guess game")
print()
name = input("Hello! What is your name: ")
print()
print("Well Mike, I am thinking of a number between 1 and 20.")
print()
number = random.randint(1, 20)
print()
for i in range(1, 6):
    guess = int(input("Take a guess:  "))

    if guess < number:
        print("Your gues is too low.")
    elif guess > number:
        print("Your number is too high")
    else:
        break


if guess == number:
    print()
    print(f"\nGood Job, {name}! you guess the number in {i} gusses.")
else:
    print()
    print(f"Bad luck {name}! The number was {i}.")