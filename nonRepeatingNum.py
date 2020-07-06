def non_repeating(str1):
    numbers = []
    ctr = {}
    for i in str1:
        if i in ctr:
            ctr[i] += 1
        else:
            ctr[i] = 1
            numbers.append(i)
    for i in numbers:
        if ctr[i] == 1:
            return i
    return None

print(non_repeating('abcdef'))
print(non_repeating('abcabcdef'))
print(non_repeating([5,6,6,8,8,5,1,2]))

# first non repeating number program