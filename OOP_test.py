# main function
def main():
    # Creating an object (ThisCar) from a class (Car)
    ThisCar = Car("ABC123", 2500)  # Setting attributes using constructor (VehicleID, EngineSize)

    # Using the setter and getter methods

    ThisCar.SetPurchasePrice(12000)  # Setting an attribute using a setter method (PurchasePrice)

    vID = ThisCar.GetVehicleID()  # Getting an attribute using a getter method
    print(vID)  # Prints the value returned by the GetVehicleID method


# Python doesn't have a record type therefore classes are used

class Car:  # Declaring the class
    def __init__(self, n, e):  # Declaring the constructor

        # Declaring the class's attributes
        # Two __ before the attribute name signifies it is private
        self.__VehicleID = n
        self.__Registration = ""
        self.__DateOfRegistration = None
        self.__EngineSize = e
        self.__PurchasePrice = 0.00


    # Declaring the class's methods
    # Setters and getters are used to set and get private attributes' values
    # No setters exist for VehicleID or EngineSize as they are set in the constructor and don't need to be reset

    # Declaring Setters
    def SetPurchasePrice(self, p):  # PurchasePrice setter
        self.__PurchasePrice = p
    def SetRegistration(self, r):  # Registration setter
        self.__Registration = r
    def SetDateOfRegistration(self, d):  # DateOfRegistration getter
        self.__DateOfRegistration = d

    # Declaring Getters
    def GetPurchasePrice(self):  # PurchasePrice getter
        return self.__PurchasePrice
    def GetRegistration(self):  # Registration getter
        return self.__Registration
    def GetDateOfRegistration(self):  # DateOfRegistration getter
        return self.__DateOfRegistration

    def GetVehicleID(self):  # VehicleID getter
        return self.__VehicleID
    def GetEngineSize(self):  #EngineSize getter
        return self.__EngineSize


if __name__ == '__main__':
    main()