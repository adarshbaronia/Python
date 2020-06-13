import random

char = list('abcdefghijklmnopqrstuvwxyz')
char.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
char.extend(list('.!@#$&^:/'))
char.extend(list("0123456789"))


length = int(input("Enter the length: "))

thepassword = ""
for i in range(length):
    thepassword += random.choice(char)

print()
print(thepassword)

