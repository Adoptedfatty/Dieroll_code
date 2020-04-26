# Python does not contain overloading
import datetime


def main():
    ThisBook = Book("Title", "Author", "ItemID")  # Creating an object (ThisBook) from class (Book)
    ThisCD = CD("Title", "Artist", "ItemID", "Genre")  # Creating an object (ThicCD) form class (CD)

    print(ThisBook.GetTitle())
    print(ThisCD.GetGenre())


# Creating an abstract class to be inherited from
class LibraryItem:  # Base class
    def __init__(self, t, a, i):  # Base class constructor method
        self.__Title = t
        self.__Author__Artist = a
        self.__ItemID = i
        self.__OnLoan = False
        self.__DueDate = datetime.date.today()

    def GetTitle(self):  # Title getter method
        return self.__Title

    # Other methods

    def Borrowing(self):  # Sets a LibraryItem's OnLoan status to True and Sets DueDate of return
        self.__OnLoan = True
        self.__DueDate = self.__DueDate + datetime.timedelta(weeks=3)
    def Returning(self):  # Resets a LibraryItem's OnLoan status to False
        self.__OnLoan = False
    def PrintDetails(self):  # Prints the details of required LibraryItem
        print("Title: ", self.__Title, "; by: ", self.__Author__Artist, "; ", end='')
        print("Item ID: ", self.__ItemID, "; On Loan: ", self.__OnLoan, "; Due Date: ", self.__DueDate)


# Creating classes to inherit
class Book(LibraryItem):  # First subclass (Parent class)
    def __init__(self, t, a, i):  # Subclass constructor method
        LibraryItem.__init__(self, t, a, i)  # Calls base class constructor method
        self.__IsRequested = False
        self.__RequestedBy = 0

    def SetIsRequested(self):
        self.__IsRequested = False
    def SetRequestedBy(self, requests):
        self.__RequestedBy = requests

    def GetIsRequested(self):
        return self.__IsRequested
    def GetRequestedBy(self):
        return self.__RequestedBy

    def PrintDetails(self):  # Method in subclass overrides base class method
        print("Book Details: ")
        LibraryItem.PrintDetails(self)  # Calls method of the same name from base class
        print("Requested By: ", self.__RequestedBy, " people")

class CD(LibraryItem):  # Second subclass (Parent class)
    def __init__(self, t, a, i, g):
        LibraryItem.__init__(self, t, a, i)
        self.__Genre = g

    def SetGenre(self, g):
        self.__Genre = g

    def GetGenre(self):
        return self.__Genre


if __name__ == '__main__':
    main()
