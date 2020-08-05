def reversed_list(lst1, lst2):
  lst3 = lst2[::-1]
  if lst3 == lst1:
      return True
  return False

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3, 11], [11, 5, 3, 1]))
print(reversed_list([1, 2, 3, 4], [4, 3, 2, 1]))