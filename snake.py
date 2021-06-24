# Step 3 - Create Snake class
from reptile import Reptile


class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.cold_blooded = True


# Add specific methods/behaviours
    def use_tongue_to_smell(self):
        return "If I can touch it, I can smell it"


# Create object of Snake class
smart_snake = Snake()
# print(smart_snake.move())  # move() is available from Animal class
# print(smart_snake.hunt())  # hunt() is available from Reptile class
# print(smart_snake.use_tongue_to_smell())  # is available from Snake class

# Go to step 4
