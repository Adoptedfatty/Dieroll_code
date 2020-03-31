# imports the library random
import random

# save paths of files used
dicesum_path = "C:\\Users\\Habashy\\Desktop\\AL CS S20\\Statistics and Probability\\Dice Rolls\\dicesum.txt"
frequencytable_path = "C:\\Users\\Habashy\\Desktop\\AL CS S20\\Statistics and Probability\\Dice Rolls\\frequencytable.txt"


# Main function executed when program is run
def main():
    repeat = input("How many times do you want to roll the dice? ")
    rollloop(int(repeat))
    frequencytable_create()




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
def rollloop(repeat=1):

    reset_dicesum()

    # loop counter sumcount of type integer
    sumcount = 1

    # saves sum of two rolled 6 sided dice to a file desired number of times
    while sumcount <= repeat:

        # increment counter
        sumcount = sumcount + 1

        write_dicesum(sum_sixsidedice())


def read_dicesum():
    dicesum_handle = open(dicesum_path, "r")
    print(dicesum_handle.read())
    dicesum_handle.close()


def write_dicesum(sum):
    dicesum_handle = open(dicesum_path, "a")  # opens dicesum file
    dicesum_handle.write(str(sum))  # appends sum of dice to a file
    dicesum_handle.write("\n")  # moves on to next line
    dicesum_handle.close()  # closes dicesum file


def reset_dicesum():
    # reset file if it already has data
    dicesum_handle = open(dicesum_path, "w")
    dicesum_handle.close()


def frequencytable_create():
    dicesum_handle = open(dicesum_path, "r")
    sumofdice = dicesum_handle.readline()

    frequencytable_list = [
        [2, 0],
        [3, 0],
        [4, 0],
        [5, 0],
        [6, 0],
        [7, 0],
        [8, 0],
        [9, 0],
        [10, 0],
        [11, 0],
        [12, 0]
    ]

    dicesum_handle = open(dicesum_path, "r")
    sumofdice_str = dicesum_handle.readline()
    sumofdice = int(sumofdice_str)
    while len(sumofdice_str) > 0:
        if sumofdice % 2 == 0:
            if sumofdice == 2:
                frequencytable_list[0][1] = frequencytable_list[0][1] + 1
            elif sumofdice == 4:
                frequencytable_list[2][1] = frequencytable_list[2][1] + 1
            elif sumofdice == 6:
                frequencytable_list[4][1] = frequencytable_list[4][1] + 1
            elif sumofdice == 8:
                frequencytable_list[6][1] = frequencytable_list[6][1] + 1
            elif sumofdice == 10:
                frequencytable_list[8][1] = frequencytable_list[8][1] + 1
            elif sumofdice == 12:
                frequencytable_list[10][1] = frequencytable_list[10][1] + 1
        else:
            if sumofdice == 3:
                frequencytable_list[1][1] = frequencytable_list[1][1] + 1
            elif sumofdice == 5:
                frequencytable_list[3][1] = frequencytable_list[3][1] + 1
            elif sumofdice == 7:
                frequencytable_list[5][1] = frequencytable_list[5][1] + 1
            elif sumofdice == 9:
                frequencytable_list[7][1] = frequencytable_list[7][1] + 1
            elif sumofdice == 11:
                frequencytable_list[9][1] = frequencytable_list[9][1] + 1

        sumofdice_str = dicesum_handle.readline()
        if sumofdice_str != '':
            sumofdice = int(sumofdice_str)

    dicesum_handle.close()

    frequencytable_handle = open(frequencytable_path, "w")

    row = 0
    while frequencytable_list[row][0] < 12:
        frequencytable_handle.write(str(frequencytable_list[row][0]))
        frequencytable_handle.write("     ")
        frequencytable_handle.write(str(frequencytable_list[row][1]))
        frequencytable_handle.write("\n")
        row = row + 1

    frequencytable_handle.close()
    print("successfully created frequency table")





main()
