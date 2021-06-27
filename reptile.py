# ### Reptile class

# #### Create a Reptile class to inherit Animal class


from animal import Animal  # From file to class. Must be in the same directory
class Reptile(Animal):    #Inheriting from Animal class
    def __init__(self):
        super().__init__() # Super in used to inherit everything from parent class
        self.cold_blooded = True
        self.tetrapods = None
        self.heart_chamber = [3,4]

    def seek_heat(self):
        return"Always look for warmth and sun"

    def hunt(self):
        return"Keep hunting to find food"

    def use_venom(self):
        return"If I haveit I'll use it"


# - Let's create an object of Reptile class
smart_reptile = Reptile()

# print(smart_reptile.breathe()) #breathe method is inherited from Animal class
print(smart_reptile.hunt()) # hunt() is available in Reptile class
# print(smart_reptile.eat())
# print(smart_reptile.move())
print(smart_reptile.hunt())

# - Go to step 3, Snake