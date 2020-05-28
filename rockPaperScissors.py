import random

print("Welcome to The Rock, Paper, Scissors Game")
#get the user Input
rounds = int(input("\nHow many rounds would you like to play: "))
print()
#Initialize variables
moves = ['rock', 'paper', 'scissors']
p_score = 0
c_score = 0
print()

#main loop
for game_round in range(rounds):
    #print the main screen and get user input
    print(f"Round  {str(game_round + 1)}")
    print(f"Player:  {str(p_score)}  \t Computer: {str(c_score)}")
    print()

    c_index = random.randint(0, 2)
    c_choice = moves[c_index]
    print()
    #get the players move
    p_choice = input("Time to pick...Rock,Paper, Scissors: ").lower().strip()
    #if the player makes a valid move
    print()
    if p_choice in moves:
        print("\tComputer: "+ c_choice)
        print("\tPlayer: " + p_choice)
        #computer chooses rock
        if p_choice == 'rock' and c_choice == 'rock':
            winner = 'Tie'
            phrase = 'it is a tie. No winner!'
        elif p_choice == 'paper' and c_choice == 'rock':
            winner = 'player'
            phrase = "Paper covers rock!"
        elif p_choice == 'scissors' and c_choice == 'rock':
            winner = 'computer'
            phrase = 'Rock smashes scissors!'
        #computer chooses paper
        elif p_choice == 'rock' and c_choice == 'paper':
            winner = 'computer'
            phrase = 'Paper covers rock!'
        elif p_choice == 'paper' and c_choice == 'paper':
            winner = 'Tie'
            phrase = "it is a tie. No winner!'"
        elif p_choice == 'scissors' and c_choice == 'paper':
            winner = 'player'
            phrase = 'scissors cuts paper.'
        #computer chooses scissors
        elif p_choice == 'rock' and c_choice == 'scissors':
            winner = 'player'
            phrase = 'Rock smashes scissors!'
        elif p_choice == 'paper' and c_choice == 'scissors':
            winner = 'computer'
            phrase = "scissors cuts paper"
        elif p_choice == 'scissors' and c_choice == 'scissors':
            winner = 'Tie'
            phrase = "It is a Tie. No winner."
        else:
            print("No winner!")
            winner = 'tie'
            phrase = "It is a tie, how boring!"
        print()
        #display round results
        print("\t " + phrase)
        print()
        if winner == 'player':
            print(f"You win round {str(game_round + 1)}.")
            p_score += 1
            print()
        elif winner == 'computer':
            print(f"Computer win round {str(game_round + 1)}.")
            c_score += 1
            print()
        else: 
            print("\tThis round was a tie.")
            print()
    else:
        print("\t This is not a valid game move.")
        print("Computer gets the point")
        c_score += 1
        print()


#game has ended. Printing resuts

print("\nFinal Game Results")
print(f"\tRounds Played: {str(rounds)}") 
print(f"\tPlayer Score: {str(p_score)}") 
print(f"\tComputer Score: {str(c_score)}") 

if p_score > c_score:
    print("\t Winner: PLAYER!!!")
elif c_score > p_score:
    print("\t Winner: COMPUTER!!!")
else:
    print("TIE!!!")




