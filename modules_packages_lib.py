# Python's extensive documentation on python.org
# We have used built-in functions and created new ones

# import is a keyword used to import any modules available in python.org
# import math  # Provides several mathematical operations
# from random import random  # Generates random number
#
# num1 = 23.44
#
# # Rounding a float depending on it's value
# # If value < .50 round it down, if value > .51 round it up
# print(math.ceil(num1))  # This will always round it up for any decimal value
# print(math.floor(num1))  # This will always round it down for any decimal value
# print(math.pi)
#
# # Random class/methods
# print(random())  # generates a random number between 0 and .99

# Interacting with our machine using python
# import os  # os is used to get info about our operating system
# import math, datetime, sys  # sys is used to get system specific info
#
# work_dir = os.getcwd()  # getcwd provides current working directory
# print(work_dir)
#
# # print(os.getuid())  # Doesn't work on Windows OS
# # print(os.cpu_count())
# # print(os.uname())  # Doesn't work on Windows OS
# # print(os.path)
#
# print(datetime.date.today())
# print(sys.path)
# # type() len()

# we can make an API call to any web address using python requests package
# pip is a package manager in python to install any packages
# pip install requests

import requests

requests_api = requests.get("https://www.bbc.co.uk/")

print(type(requests_api.status_code))  # 200 - success; 404 and above - error
if requests_api.status_code == 200:
    print("Success")
print(type(requests_api.headers))  # display website headers
# print(requests_api.content)

