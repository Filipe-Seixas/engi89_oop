# Python Object-Oriented Programming
## Four Pillars of OOP
### Functions and good practice of functions
#### DRY - Don't Repeat Yourself
- Syntax:   def function_name(parameter1, parameter2):

```python
# First Iteration
def greeting():
    print("Welcome on board! Enjoy your trip.")
# pass allows the interpreter to escape the function without errors

greeting()  # You need to call the function for it to execute
```
```python
# Second iteration using RETURN statement
def greeting():
    print("Good morning")
    return "Welcome on board! Enjoy your trip."

print(greeting())
```
```python
# Third iteration with user name as a string as an argument
def greeting(name):
#    print(name)
    return "Welcome on board " + name

print(greeting("James"))  # We need to pass an argument for the name parameter
```
```python
# Create a function to prompt the user to enter their name and display the name back to the user with greeting message
def greetings(name):
    return "Welcome " + name

user_name = input("Please tell me your name:  ")
print(greetings(user_name))
```
```python
# Create a function with multiple args as an int
def add(num1, num2):
    return num1 + num2

print(add(9, 3))

def multiply(num1, num2):
    return num1 * num2
    # Any code after return (that is inside the function) will not execute

print(multiply(2, 3))
```

#### Python Modules, packages and Lib
- *Python's extensive documentation on [python.org](https://docs.python.org/3/library/)*

```python
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
```
```python
# Interacting with our machine using python
import os  # os is used to get info about our operating system
import math, datetime, sys  # sys is used to get system specific info

work_dir = os.getcwd()  # getcwd provides current working directory
print(work_dir)

# print(os.getuid())  # Doesn't work on Windows OS
# print(os.cpu_count())
# print(os.uname())  # Doesn't work on Windows OS
# print(os.path)

print(datetime.date.today())
print(sys.path)
# type() len()
```
- Install requests using pip
- `pip install requests`
- we can make an API call to any web address using python requests package
- pip is a package manager in python to install any packages
- To check version `pip -V`

```python
import requests

requests_api = requests.get("https://www.bbc.co.uk/")

print(type(requests_api.status_code))  # 200 - success; 404 and above - error
if requests_api.status_code == 200:
    print("Success")
print(type(requests_api.headers))  # display website headers
# print(requests_api.content)
```

## Four Pillars os OOP
### Abstraction

- 
- 
### Inheritance

- 
- 
### Encapsulation

- 
- 
### Polymorphism

- 
- 


- step one create animal.py file to create a parent class
- step two create reptile.py to abstract data and inherit from animal.py
- step three create snake.py
- step four create python.py and at this point we should be able to utilise inheritance from multiple 
  classes - everything available from animal class to python