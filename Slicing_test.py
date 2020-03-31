# slicing test
# slicing part of a list or string using an upper and/or lower bound
# counting starts from 0

# slicing a list
list1 = ["a", "b", "c", "d", "e", "f", "g"]
print(list1[1:4])  # lower bound 1 (between 1st and 2nd elements), upper bound 4 (between 4th and 5th elements)
print(list1[:3])  # no lower bound, upper bound 3
print(list1[2:])  # lower bound 2, no upper bound
print(list1[-1:])  # lower bound -1 (last element), no upper bound
print(list1[:-2])  # no lower bound, upper bound -2 (second to last element)

# slicing a string
string1 = "abcdefg"
print(string1[1:4])
print(string1[:3])
print(string1[2:])
print(string1[-1:])
print(string1[:-2])

# accessing a single character
print(string1[1])  # accesses the 2nd character
