import math

print("Welcome to the Factorial Calculator App")
print()
fact_number = int(
    input("What number would you like to compute the factorial of?  "))
# here this for is to print how facorial happen
print(str(fact_number) + "!  =", end="")
for i in range(1, fact_number):
    print(str(i), end='*')
print(str(fact_number), end='')

print()
print()
print("Here is the result from the math library: ")
f1 = math.factorial(fact_number)
print(f"The factorial of {fact_number}! is {f1}")
print()

print("Here is the result from my own algorithim: ")

f2 = 1
for i in range(1, fact_number + 1):
    f2 = f2 * i
print(f"The factorial of {fact_number}! is {f2}")
print()
print("Thank you!!")
