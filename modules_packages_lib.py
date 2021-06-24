# Python's extensive documentation on python.org
# We have used built-in functions and created new ones

# import is a keyword used to import any modules available in python.org
import math  # Provides several mathematical operations
from random import random  # Generates random number

num1 = 23.44

# Rounding a float depending on it's value
# If value < .50 round it down, if value > .51 round it up
print(math.ceil(num1))  # This will always round it up for any decimal value
print(math.floor(num1))  # This will always round it down for any decimal value
print(math.pi)

# Random class/methods
print(random())  # generates a random number between 0 and .99

