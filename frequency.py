from collections import Counter

print("Welcome to the Frequency Analysis App")
print()
non_letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',' ,'.' , '?' , '!' , "'" , '"' , ";", ":", '(', ")"," "]
key_phrase_1 = input("Enter a word or phrase: ").lower().strip()
for non_letter in non_letters:
    key_phrase_1 = key_phrase_1.replace(non_letter, '')

total_occurrences = len(key_phrase_1)
#create a counter object to telly the number of each letter
letter_count = Counter(key_phrase_1)

print("\nHere is the frequency analysis from key phrase 1: ")
print("\n\tLetter\t\tOccurrence\tPercentage")
for key, value in sorted(letter_count.items()):
    percentage = 100 * value/total_occurrences
    percentage = round(percentage, 2)
    print("\t" + key + "\t\t" + str(value) + "\t\t" + str(percentage) + "% ")

#make a list of letters from higest occurrence to lowest
ordered_letter_count = letter_count.most_common()
key_phrase_1_ordered_letters = []
for pair in ordered_letter_count:
    key_phrase_1_ordered_letters.append(pair[0])

#print the list
print("\nLetters ordered from highest occurrence to lowest: ")
for letter in key_phrase_1_ordered_letters:
    print(letter, end=' ')