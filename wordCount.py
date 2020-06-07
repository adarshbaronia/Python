import operator

words = input("Input some text:  ")
wordlist = words.split()
wordcount = len(wordlist)
print(wordcount)

worddict = {}
for word in wordlist:
    if word in worddict:
        worddict[word] += 1
    else:
        worddict[word] = 1


sortedword = sorted(worddict.items(), key=operator.itemgetter(1), reverse = True)

for word, count in sortedword:
    print(f"{word}:  {count}")
