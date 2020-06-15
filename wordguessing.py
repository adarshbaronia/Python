import random

print("Welcome to the Guess My word App\n")
#create a dict to hold the words
game_dict = {
    "sports":['basketball','baseball','soccer','foootball','tennis','curling','criket', 'racing', 'running','boxing','wrestling'
    ],
    "colors":[
        'orange','yellow','purple','aquamarine','violet','gold','olive','red','black'
        ],
    "fruits":[
        'apple','banana','watermelon','peach','mango','strawberry','apricot','coconut','blackberry','jackfruit','pineapple','pomegranate','tamarind'
    ],
    "classess":['english','mathematics','history','health','programming'
    ],
    "country":['india','france','america','canada','australia','germany','norway','singapour','thailand'
    ]
}

#create a list of keys
game_keys =[]
for key in game_dict.keys():
    game_keys.append(key)

#main game
playing = True
while playing:
    #randomly pick a game word and category from dict
    game_category = game_keys[random.randint(0,len(game_keys) - 1 )]
    game_word = game_dict[game_category][random.randint(0,len(game_dict[game_category])-1)]
    #build a dashed word to represent the game word
    blank_word = []
    for letter in game_word:
        blank_word.append("-")

    print(f"Guess a {str(len(game_word))} letter word from the following category: {game_category}")
    guess = ""
    guess_count = 0

    #a single round loop
    while guess != game_word:
        print("".join(blank_word))
        guess = input("\nEnter your guess: ").lower()
        guess_count += 1

        #guess is correct, user won the game
        if guess == game_word:
            print(f"\nCorrect! You guesses the word in {str(guess_count)} guesses.")
            break

        else:
            print("That is not correct. Try again with a hint!")
            #loop to replace '- in blank word to reveal a letter for hint
            swapping = True
            while swapping:
                letter_index = random.randint(0, len(game_word)-1)
                if blank_word[letter_index] == "-":
                    blank_word[letter_index] = game_word[letter_index]
                    swapping = False

    choice = input("\nWould you like to play again (y/n): ").lower()
    if choice != 'y':
        playing =False
        print()
        print("Hope you enjoyed the game. GoodBye!")




















        



    

