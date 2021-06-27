# ### Snake class

# #### Create a Snake class

from reptile import Reptile

class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.cold_blooded = True


    def use_tongue_to_smell(self): # Adding some specific methods/behaviours
        return " *Hiss* "

#
smart_snake = Snake()
# print(smart_snake.move()) # move() is available from Animal class
# print(smart_snake.hunt())# hunt () is available from Reptile class

# - Checking members from Snake class
print(smart_snake.forked_tongue) # Should output True
print(smart_snake.use_tongue_to_smell()) # Should output *hiss*

# - Checking members from Reptile class
print(smart_snake.tetrapods) # Should output *hiss*
print(smart_snake.hunt()) # Should output Keep hunting for food

# - Checking members from Animal class
print(smart_snake.eyes) # Should output True
print(smart_snake.breathe()) # Should output Keep breathing, stay alive

# - Go to step 4, Python