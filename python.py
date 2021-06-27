# ### Python class

# #### Create a Python class

from snake import Snake

class Python(Snake):
    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True


    def digest_large_prey(self):
        return "I can dislocate my jaw to eat you"

    def climb(self):
        return "Can't even escape me from high in trees"

    def shed_skin(self):
        return "I'm growing out of my skin"

fast_python = Python()
print(fast_python.climb())
print(fast_python.hunt())
print(fast_python.move())
print(fast_python.use_tongue_to_smell())
print(fast_python.shed_skin())