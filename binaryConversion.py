# program to convert decimal to binary and hexa decimal

max_value = int(input("\nCompute binary and hexadecimal up to this number: "))
decimal = list(range(1, max_value+1))
binary = []
hexadecimal = []
# appenindg range in lists
for num in decimal:
    binary.append(bin(num))
    hexadecimal.append(hex(num))
print("generating lists...")
print()
print("\nUsing slices, we will now show a portion of each list. ")

# asking for number index to show the conversion #from within max value above
lower = int(input("enter first number in range: "))
upper = int(input("enter last number in range: "))

# priniting decimals
print("\nDecimal values from" + str(lower) + "to" + str(upper) + ":")
for num in decimal[lower-1:upper]:
    print(num)

# printing binary
print("\nBinary values from" + str(lower) + "to" + str(upper) + ":")
for num in binary[lower-1:upper]:
    print(num)

# printing hexadecimal
print("\nHexadecimal values from" + str(lower) + "to" + str(upper) + ":")
for num in hexadecimal[lower-1:upper]:
    print(num)
print()

input("\nPress enter to seel values from 1 to " + str(max_value) + ":")
print("Decimal-----Binary-----Hexadecimal")
print()

for d, b, h in zip(decimal, binary, hexadecimal):
    print(str(d)+"-----"+str(b)+"-----"+str(h)) 
