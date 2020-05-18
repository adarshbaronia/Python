print("Welcome to the fibonacci Calculator App")
print()

num = int(input("Enter the number for fibonacci Squence: "))

fib = [1, 1]
for i in range(num - 2):
    new_fib = fib[i]+fib[i+1]
    fib.append(new_fib)

print()
# display the fib values
print(f"The first {num} numbers in fibonacci sequence are: ")
for number in fib:
    print(number)

print()
# golden ratio
golden = []
for i in range(len(fib)-1):
    ratio = fib[i+1] / fib[i]
    golden.append(ratio)

print("The corresponding Golden ration: ")
for number in golden:
    print(number)

print()
print("The ratio of consecutive Fibonacci terms approaches Phi: 1.618")
