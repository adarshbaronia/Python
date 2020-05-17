import cmath
#details about Quadratic equation
print("Welcome to the Quadratic Solver App.")
print()
print("A quadratic equation is of the form ax^2 + bx + c =0 ")
print("Your solution can be real or complex numbers")
print("A complex number has two parts: a + bj ")
print("Where a is thereal portion and bj is the imginary portion")
print()
qurd_equation = int(input("How many equations would yu like to solve today: "))
#sloving problem with initating a loop
for i in range(qurd_equation):
    print("Solving equation #" + str(i+1))
    print("-------------------------")
    print()
    #ask for user inputs
    a = float(input("/tPlease enter your value of a (coefficient of x^2): "))
    b = float(input("Please enter your value of b (coefficient of x): "))
    c = float(input("Please enter your value of c (coefficient): "))
    print()
    print(f"The solution to {a}x^2 + {b}x + {c} are: ")
    print()
    # showing the results
    x1 = (-b + cmath.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - cmath.sqrt(b**2 - 4*a*c))/(2*a)
    print()
    print("\n\tx1   =   "+str(x1))
    print("\n\tx2   =   "+str(x2))
    print()
    print("Thank you for using our App!")
