
#Exercise 1: Import the math module and print the value of pi
import math
print(math.pi)
print()

#Exercise 2: Use math.sqrt() to calculate the square root of a number
print("Square root of 25 using math.sqrt():")
print(math.sqrt(25))
print()

#Exercise 3: Use the random module to generate a random number between 1 and 100
import random
print("Random number between 1 and 100:")
print(random.randint(1, 100))
print()

#Exercise 4: Use datetime to get the current date and time
import datetime
print("Current date and time:")
print(datetime.datetime.now())
print()

#Exercise 5: Use calendar to print the calendar of a given month and year
import calendar
print("Calendar of May 2025:")
print(calendar.month(2025, 5))
print()

#Exercise 6: From the math module, import only the factorial function
from math import factorial
print("Factorial of 5 using imported factorial:")
print(factorial(5))
print()

#Exercise 7: From datetime, import date and print today's date
from datetime import date
print("Today's date:")
print(date.today())
print()

# Exercise 8 & 9: Create a Python file called `my_utils.py` with a function add(a, b)
# and import `add` in another script and use it
# Exercise 10: Add another function to `my_utils.py` (e.g., is_even) and use it
print("Using functions from my_utils.py:")
from my_utils import add, is_even
print("add(3, 7):", add(3, 7))
print("is_even(10):", is_even(10))
print()

# Exercise 11: Use the os module to print the current working directory
import os
print("Current working directory:")
print(os.getcwd())
print()

#Exercise 12: Use the sys module to print command-line arguments
import sys
print("Command-line arguments:")
print(sys.argv)
print()

#Exercise 13: Use time.sleep() to delay execution for 3 seconds
import time
print("Sleeping for 3 seconds...")
time.sleep(3)
print("Awake now!")
print()

#Exercise 14: Use dir() on the math module to list all available functions
print("dir(math):")
print(dir(math))
print()

#Exercise 15: Use help() on a specific function like random.randint
print("help(random.randint):")
help(random.randint)
