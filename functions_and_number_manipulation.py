# functions

# string functions
ThisString = "ABCDEFG"
ThisString[2]  # access a single character in the position required (counting starts from 0)
len(ThisString)  # returns the length of a desired String

# character functions
a_character = chr(97)  # returns character associated with the character code (97 returns the character a)
a_code = ord("a")  # returns character code associated with the character (character a has character code 97)

# date and time functions
from datetime import *  # imports date/time library

Somedate = date(2020, 3, 28)  # set date (year, month, day)
Today = date.today()  # reads system clock for date
day = 1
Somedate = Somedate + timedelta(day)  # adds days to desired date

Sometime = datetime(2020, 3, 28, 6, 25)  # set date and time (year, month, day, hour, minute, second)
Now = datetime.now()  # reads system clock for date and time
hour = 1
Sometime = Sometime + timedelta(day, 0, 0, 0, 0, hour)  # adds days and hours to desired time


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////


# number manipulation

# rounding numbers
round(2.554, 0)  # rounds the number 2.554 after 0 decimal places (result is 3)
round(2.554, 0)  # rounds the number 2.554 after 1 decimal places (result is 2.6)
round(2.554, 0)  # rounds the number 2.554 after 2 decimal points (result is 2.55)

# truncating numbers
int(2.554)  # removes any numbers after the decimal point (result is 2)

# converting strings into numbers
int("2")  # converts a string into an integer
float("2.2")  # converts a string into a float

# formatting numbers for output
print("{0:>10} {1:^10} {2:<10} {3:.2f}".format(10, 20, 30, 18.2))
# check textbook page 204

# random number generator
import random  # imports random library
random.randint(1, 6)  # picks a random integer between 1 and 6 (including the bounds)
random.choice(["a", "b", "c"])  # picks a random element from a list
random.random()  # generates a random float between 0 and 1
