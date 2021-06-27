# ### Animal class

# -  follow the correct naming convention
# we need to initialise with build it method called __init__(self)
# - self refers to current class

class Animal:       #We declare attributes in out init method
     def __init__(self):
         self.aline = True
         self.spine = True
         self.eyes = True
         self.lungs = True

     def breathe(self):
         return ("Keep breathing, stay alive")

     def eat(self):
         return "Time to eat"

     def move(self):
         return "Dance"


# - We need to create an object of this class in order to use any methods
# - For cat as a user the functionality inside Animal class and the method breathe is abstracted
#cat = Animal()
#print(cat.eat())

# - Go to step 2, Reptile
