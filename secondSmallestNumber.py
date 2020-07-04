def second_largest(numbers):
    m1 = float('inf')
    m2  = float('inf')
    for x in numbers:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2

print(second_largest([5,6,8,9,4,2]))
print(second_largest([15,56,11,89,23,-20]))
print(second_largest([-25, -56, -20, -80, -55]))