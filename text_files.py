# modes of access: "a" for append, "w" for write, "r" for read, "w+" for read/write
# reading from/writing to text files test
path = "C:\\Users\\Habashy\\Desktop\\AL CS S20\\Tests\\SampleFile.txt"


# writing to text files (overwrites existing data)

# opening a text file (if file doesn't exist: creates new file)
FileHandle = open(path, "w")  # path, mode of access ("w" for write)
# writing to the file
FileHandle.write("I am\nno\nlonger\nasking")  # \n to move to the next line
# closing the file
FileHandle.close()


# reading from text files

# opening the file
FileHandle = open(path, "r")  # path, mode of access ("r" for read)
# reading from the file
LineOfText = FileHandle.readline()  # reads one line of text (repeated use reads subsequent lines)
BlockOfText = FileHandle.read()  # reads whole file (ignores lines already read by FileHandle.readline())
LineList = FileHandle.readlines()  # returns file as a list where each line is an element
# closing the file
FileHandle.close()
print("Data read from Sample file: \n", end="")
print(LineOfText, end="")
print(BlockOfText)


# appending to text files (adds to existing data)

# opening the file
FileHandle = open(path, "a")  # path, mode of access ("a" for append)
# appending data
FileHandle.write("\n*pulls out gun*")
# closing the file
FileHandle.close()


# end-of-file (EOF) marker

path = "C:\\Users\\Habashy\\Desktop\\AL CS S20\\Tests\\EOFtest.txt"
FileHandle = open(path, "r")
LineOfText = FileHandle.readline()
print("\nData read from EOF file: \n")
while len(LineOfText) > 0:
    print(LineOfText)
    LineOfText = FileHandle.readline()
FileHandle.close()
