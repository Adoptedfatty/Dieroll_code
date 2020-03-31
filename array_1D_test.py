# there are no arrays in python therefore a list is used instead
# lists don't have a definite data type
# list test

# initializing a list
List1 = []
# adding elements to the list
List1.append("peepee")
List1.append("poopoo")
List1.append(" ")
# printing list elements
"""print(List1[0], "in", List1[1])"""

# initializing a list with elements
List2 = [0, 1, 2, 3, 4, 5]
# printing elements
"""for i in List2:
    print(List2[i]) """

# initializing a list using a loop
# puts the element 0 in List3 locations 0 to 9
List3 = [0 for i in range(10)]
# printing elements
"""for i in List3:
    print(List3[i])"""

#range of list
rng = 5
# initializing a list using multiplication
AList = ["pp"] * rng
# printing elements
"""for i in range(rng):
    print(AList[i])"""

# writing to a list
List1[2] = "xd"
# printing a whole list
"""print(List1)"""
