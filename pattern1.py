height = int(input("Enter height: "))

for i in range(1, height + 1):
    line = i * ' *'
    print(line)



for i in range(1, height + 1):
    line = (height - i) * ' ' + i * '* '
    print(line)