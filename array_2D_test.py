# there are no 2D arrays in python therefore a list of lists (2D list) is used
# 2D list test

# using a 2D array to represent a game board of 6 rows and 7 columns
# initializing a 2D list

# using conventional method
Board1 = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
         ]

# OR

# using a loop
rows = 6
columns = 7

Board2 = [
            [0 for i in range(columns)] for j in range(rows)
         ]

# OR

# using multiplication
rows = 6
columns = 7

Board3 = [[0] * columns] * rows



# writing to a 2D list
Board1[1][2] = 5  # changes value of element in row 2 column 3
Board1[1][3] = 6  # changes value of element in row 2 column 4

