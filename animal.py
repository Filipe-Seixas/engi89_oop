# Step 1 - Create Animal class

class Animal:  # follow CamelCase naming convention
    # we need to initialise class with built in method called __init__(self)
    # self refers to current class
    def __init__(self):  # we declare attributes in our init method
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        return "Keep breathing to stay alive!"

    def eat(self):
        return "Time to eat."

    def move(self):
        return "Move left and right to stay awake."


# we need to create an object of this class in order to use any of the methods
# print(eat()) would not work
cat = Animal()  # creating an object of Animal class
# for cat as a user the functionality inside Animal class and the method breathe is abstracted
# print(cat.breathe())
# print(cat.eat())

# Go to step 2
