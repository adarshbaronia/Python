def reverse_words_order_and_swap_cases(sentence):

    count1 = 0
    count2 = 0
    count3 = 0
    newword = ''
    for i in sentence:
        if (i.isupper()) == True:
            count1+= 1
            newword += i.lower()
        elif (i.islower()) == True:
            count2 += 1
            newword += i.upper()
        elif (i.isspace()) == True:
            count3 += 1
            newword += i

    word = newword.split(' ')
    reverseword = ' '.join(reversed(word))
    return reverseword
     


print(reverse_words_order_and_swap_cases('rUns dOg'))
    



