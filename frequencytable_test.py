dicesum_path = "C:\\Users\\Habashy\\Desktop\\AL CS S20\\Statistics and Probability\\Dice Rolls\\dicesum.txt"
frequencytable_path = "C:\\Users\\Habashy\\Desktop\\AL CS S20\\Statistics and Probability\\Dice Rolls\\frequencytable.txt"

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
