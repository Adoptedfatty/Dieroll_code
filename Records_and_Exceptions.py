# Python doesn't have a record type therefore classes are used instead

class CarRecord:
    def __init__(self):  # Initialiser method for the class
        self.VehicleID = ""  # No __ means attribute is public
        self.Registration = ""
        self.DateOfRegistration = None
        self.EngineSize = 0
        self.PurchasePrice = 0.00


def main():
    ThisCar = CarRecord()  # Makes object (ThisCar) from class (CarRecord)
    ThisCar.EngineSize = 2500  # Setting value to attribute (EngineSize) of object (ThisCar)

    ThisOtherCar = CarRecord()
    Car = [ThisOtherCar for i in range(0, 100)]  # Makes a list (array) of 100 car records
    Car[0].EngineSize = 3000  # Assigns value to attribute (EngineSize) of the first car in the list

    ExceptionHandle()


# Exception Handling

def ExceptionHandle():
    NumberString = input("Enter an integer: ")  # Prompts user to enter an integer value
    try:  # Tries to convert entered number into integer and print it
        n = int(NumberString)
        print(n)
    except:  # If failed then the value was not an integer and the except is carried out
        print("This was not an integer")


main()
