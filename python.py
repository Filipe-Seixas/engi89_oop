# Step 4 - Create Python class
from snake import Snake


class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True

    def digest_large_prey(self):
        return "I can digest anything without chewing."

    def climb(self):
        return "Up we go..."

    def __shed_skin(self):  # Encapsulation hides this method from everywhere (__ before the name)
        return "I'm growing out of my skin."


# Create object of Python class
fast_python = Python()
# Using different methods from different classes can be used due to inheritance
# print(fast_python.breathe())
# print(fast_python.hunt())
# print(fast_python.use_tongue_to_smell())
# print(fast_python.climb())


