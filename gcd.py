def gcd(m, n):
    fm = []
    for i in range(1, m+1):
        if (m%i) == 0:
            fm.append(i)

    fn = []
    for j in range(1, n+1):
        if (n%j) == 0:
            fn.append(j)

    cf = []
    for f in fm:
        if f in fn:
            cf.append(f)

    return(cf[1:])


print(gcd(14,63))
print(gcd(10,100))
print(gcd(15,60))
print(gcd(99, 999))
print("***********")


def gcdOne(m, n):
    cf = []
    for i in range(1,min(m, n)+ 1):
        if (m%i) == 0 and  (n % i) ==0:
            cf.append(i)

    return(cf[1:])


print(gcdOne(14,63))
print(gcdOne(10,100))
print(gcdOne(15,60))
print(gcdOne(99, 999))
print("*************")

#witout list
def gcdTwo(m, n):
    
    for i in range(1, min(m, n)+ 1):
        if (m%i) == 0 and  (n % i) ==0:
            cf = i

    return(cf)

print(gcdTwo(14,63))
print(gcdTwo(10,100))
print(gcdTwo(15,60))
print(gcdTwo(99, 999))
print("*************")



def gcdThree(m, n):
    i = min(m, n)

    while i > 0:
        if (m%i) == 0 and (n%i) == 0:
            return(i)
        else:
            i = i + 1

print(gcdThree(14,63))
print(gcdThree(10,100))
print(gcdThree(15,60))
print(gcdThree(99, 999))
print("*************")