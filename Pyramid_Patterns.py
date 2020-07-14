# number =int(input("enter the number of rows: "))

# for i in range(1, number+1):
#     for j in range(1, i+1):
#         print("*", end='')
#     print('')


# pattern in add nubers
# number =int(input("enter the number of rows: "))
# k = 1

# for i in range(1, number+1):
#     for j in range(1, k+1):
#         print("*", end='')
#     k += 2
#     print()



# Pattern in  pyramid shape
# number =int(input("enter the number of rows: "))

# for i in range(0,number):
#     for j in range(0, number - i - 1):
#         print(end=' ')
#     for j in range(0, i+1):
#         print("*", end=' ')
#     print()

#Patter in pyramid shape with functon

def pyramid(rows):
    for i in range(rows):
        print(''*(rows - i - 1) + '*'  *(2*i+1))


print(pyramid(4))












