import random

def dice_sides():
    """ Ask the user how many sides on their die"""
    sides = int(input("\nHow many sides would you like on your dice: "))
    return sides


def dice_number():
    """ Ask the user how many dice to roll"""
    number = int(input("How many dice would you like to roll: "))
    return number


def roll_dice(sides, number):
    """ Simulate rolling the dice"""
    dice = []
    print(f"\nYou rolled {str(number)}, {str(sides)} sides dice.")
    print("\n----Results are as followed----")
    for i in range(number):
        value =random.randint(1, sides)
        print(f"{str(value)}")
        dice.append(value)
    return dice


def sum_dice(dice):
    """Add all values of dice in a list"""
    #print(f"The total value of your roll is {str(sum(dice))}.")
    total = 0
    for die in dice:
        total += die
    print(f"The total value of your roll is {str(total)}.")


def roll_again():
    """Ask the user to roll again"""
    choice = input("\nWould ou like to roll again (y/n): ").lower()
    if choice != 'y':
        roll = False
    else:
        roll = True
    return roll


#the main code
print(f"Welcome to the Python dice game App!")
rolling = True
while rolling:
    #get the info for the type of dice
    d_sides = dice_sides()
    d_number = dice_number()

    #Rolling the dice
    my_dice = roll_dice(d_sides, d_number)
    sum_dice(my_dice)

    rolling = roll_again()
print("Thank you. GoodBye!")