def arraycheck(nums):

    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]== 2 and nums[i+2]==3:
            return True
    return False


print(arraycheck([1,2,3,4,5]))
print(arraycheck([1,1,2,2,3,3]))
print(arraycheck([1,1,2,4,1]))
print("***************")


def stringbits(mystring):

    result = ''
    for i in range(len(mystring)):
        if i % 2 == 0:
            result = result + mystring[i]
    return result


print(stringbits('Hello'))
print(stringbits('Hi'))
print(stringbits('Heeololeo'))

print("************")

def end_other(a, b):
    b=a.lower()
    a=b.lower()

    #return (b.endswith(a) or a.endswith(b))
    return a[-(len(b)):] == b or a == b[-len(a):]
print(end_other("Hiabc", 'abc'))
print(end_other("ABC", 'Hiabc'))
print(end_other("abc", 'abxabc'))



print("******************")



def doublechar(mystring):
    result = ''
    for char in mystring:
        result += char * 2
    return result


print(doublechar('The'))
print(doublechar('Thee'))
print(doublechar('There'))

print("****************")

def no_teen_sum(a, b, c):

    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
    if n in [13, 14, 15, 17, 18, 19]:
        return 0
    return n

print(no_teen_sum(2,1,14))
print(no_teen_sum(19,1,14))
print(no_teen_sum(23,11,1))
print("*************")

#return the number of integer
def count_evens(nums):
    count = 0

    for element in nums:
        if element % 2 ==0:
            count += 1
    return count

print(count_evens([2,1,12,11,30,4]))
print(count_evens([12,1,2,10,30,5]))








