# Processing records sequentially

import pickle  # Library required to create binary files


class CarRecord:
    def __init__(self):  # Initialiser method for the class
        self.VehicleID = ""  # No __ means attribute is public
        self.Registration = ""
        self.DateOfRegistration = None
        self.EngineSize = 0
        self.PurchasePrice = 0.00


def sequentialmain():
    ThisCar = CarRecord()
    Car = [ThisCar for i in range(100)]


    CarFile = open('Cars.DAT', 'wb')  # Opens file for binary write (file name, method of access)

    for i in range(100):  # Loop for each array element
        pickle.dump(Car[i], CarFile)  # Write a whole record to the binary file

    CarFile.close()  # Closes file


    CarFile = open('Cars.DAT', 'rb')  # Opens file for binary read (file name, method of access)

    Car = []  # Start with empty list
    while len(CarFile.readline()) > 0:  # Check for EOF (end of file)
        Car.append(pickle.load(CarFile))  # Appends record from file to end of list

    CarFile.close()
    

# Processing random-access records

def randommain():
    ThisCar = CarRecord()


    CarFile = open('Cars2.DAT', 'rb+')  # Opens file for binary read and write

    Address = hash(ThisCar.VehicleID)  # Return the hash value of an object (VehicleID), used to compare dictionary keys using a dictionary look up feature
    CarFile.seek(Address)
    pickle.dump(ThisCar, CarFile)  # Writes a whole record to the binary file

    CarFile.close()


    CarFile = open('Cars2.DAT', 'rb')  # Opens file for binary read

    Address = hash(ThisCar.VehicleID)
    CarFile.seek(Address)
    ThisCar = pickle.load(CarFile)  # Loads record from file

    CarFile.close
    
    
    # Pseudocode
    OPENFILE <filename> FOR RANDOM/READ/WRITE/APPEND
    FILEWRITE <filename>, <var1>, <var2>
    FILEREAD <filename>, <var1>, <var2>
    SEEK <filename>, <address>
    PUTRECORD <filename>, <identifier> 
    GETRECORD <filename>, <identifier>
    EOF <filename>
    EXISTS <filename>
    CLOSEFILE <filename>
