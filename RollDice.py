# imports the library random
import random


# Main function executed when program is run
def main():
   rollloop(1000)




# Function DieRoll simulates rolling a single die
# Parameter sides decides number of sides of the die being rolled
# Variable sides of type Integer
def dieroll(sides):

    # Generates a random number between 1 and number of sides of die which is stored in integer rollresult
    # Variable rollresult of type Integer
    rollresult = random.randint(1, sides)

    # returns result of die roll
    return rollresult


# Sums results of two simultaneous 6 sided dice rolls
def sum_sixsidedice():

    # sets number of sides to 6 to simulate a 6 sided die
    sides = 6

    # simulates rolling of two dice
    # roll1, roll2 of type Integer
    roll1 = dieroll(sides)
    roll2 = dieroll(sides)

    # adds result of rolling
    # sumofdice of type Integer
    sumofdice = roll1 + roll2

    # returns sum of die rolls
    return sumofdice


# rolls 2 dice and sums their result desired number of times
# parameter repeat indicates number of desired results (default = 1)
# repeat of type Integer
def rollloop(repeat = 1):

    # loop counter sumcount of type integer
    sumcount = 1

    # prints sum of two rolled 6 sided dice desired number of times
    while sumcount <= repeat:

        # increment counter
        sumcount = sumcount + 1
        # print sum of two six sided dice
        print(sum_sixsidedice())


main()