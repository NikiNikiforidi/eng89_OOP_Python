# ### Animal class

# -  follow the correct naming convention
# we need to initialise with build it method called __init__(self)
# - self refers to current class

# **When you create a new object, the whole class is copied (and saved to the new object) and the SELF argument inside the copied class is replaced wit h he name of the new object**

class Animal:       # we declare attributes in out init method
     def __init__(self):
         self.alive = True
         self.spine = True
         self.eyes = True
         self.lungs = True

     def breathe(self):
         return ("Keep breathing, stay alive")

     def eat(self):
         return "Time to eat"

     def move(self):
         return "Dance"


# - We need to create an object of this class in order to use any methods or attributes
# - For cat (object) as a user the functionality inside Animal class and the method breathe is abstracted

# cat = Animal() # An INSTANCE is when you call a class
# print(cat.alive) # Calling an attribute
# print(cat.eat()) # Calling a method
# print(cat.move())


# ### Example for better understanding of classes and object.
# - An object basically copies the whole class to itself.
# - You can then customise members (attributes and methods) in the new object and they will be uneffected in the original class.

object = Animal() # Creating a new object

# Printing the method alive from the Animal class and the new onject
print(object.alive)
print(Animal().alive)

object.alive = False # Changing the alive method in the new object

# Re-printing the same method. Notice in Animal it is unchanged

print(object.alive)
print(Animal().alive)







# - Go to step 2, Reptile
