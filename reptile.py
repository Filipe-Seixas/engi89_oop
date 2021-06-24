# Step 2 - Create reptile class to inherit Animal class
from animal import Animal  # we need to import Animal class from the animal file


class Reptile(Animal):  # inheriting from Animal class

    def __init__(self):
        super().__init__()  # super is used to inherit everything from the parent class
        self.cold_blooded = True
        self.tetrapods = None
        self.heart_chamber = [3, 4]

    def seek_heat(self):
        return "It's chilly looking, have fun in the sun"

    def hunt(self):
        return "Keep working hard to find food"

    def use_venom(self):
        return "If I have it, I'll use it"


# create an object of reptile class
smart_reptile = Reptile()
# print(smart_reptile.breathe())  # breathe method is inherited from Animal class
# print(smart_reptile.hunt())  # hunt() is available in reptile class

# Go to step 3
