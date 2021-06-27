## Python OOP

### Functions
- Syntax def is used to declare followed by the name of the function()


#### First iteration, using PRINT
```
def greeting():
    print("Welcome and enjoy the trip!")
#pass # Pass = keyword. Allows interpreter to skip without causing errors
```

- To use a function you need to 'call' it.
- Once called, everything in the function will be interpreted
```
greeting ()
print (greeting())
```


#### Second iteration, using RETURN
```
def greeting():
    print("Kalimera")
    return "Welcome and enjoy your trip!"

print(greeting())
```


 #### Third iteration, with user name as str and arguments
```
 def greeting(name):  # The argument is what is inside the brackets
     return "Welcome on board " + name.title()

 print(greeting("niki"))
```
 **TASK: Create a function to prompt a user to enter name and display back with greeting**

```
 def greeting(name):
     return f"Welcome {name.title()}!! I am a greeting message..."

print(greeting(input("Please enter your name: ")))
```
-Teachers version:
```
 user_name = input ("Please enter your name: ")
 def greeting (name):
     return "Welcome on board " + name

print( greeting(user_name))
```

- Lets create a function with multiple argum.
```
def add(num1, num2):
    return num1 + num2

print(add(1,2))
```


- Order inside function matters, RETURN goes last
```
def multiply(num1,num2):
    return num1 * num2
    print("This function multiplies 2 numbers")
print(multiply(3,3))
```
- Correct order
```
def multiply(num1,num2):
    print("This function multiplies 2 numbers")
    return num1 * num2
print(multiply(3,3))
```

### Modules, packages and files in python
**Pythons extensive documentation on python.org**
- IMPORT is the keyword used to Import and modules available
#### Math
```
import math
import random #Generates random number
num1 = 23.44
```

- Real life situation you have to round the figure depending on the value.
- If the value is less than .50 round it down 23.0, if 23.51 then round it up.
```
print(math.ceil(num1)) #Rounds up to 24
print(math.floor(num1)) #Round down to 23
```

- Random call/methods
```
print(random.random()) #Number changes everytime you run between .0-.99

print(math.pi)
```

- Another way to add library
```
from random import random
print(random()) #Don't need to use '.random'
```

####Let's see how to interact with our machine using python import os
```
import math

import datetime
import os
import sys # sys is used to get system specifications

work_dir = os.getcwd() # provides the currently location/path
print(work_dir)
```

- linux/Mac
```
print(os.getuid())
print(os.uname())
print(os.cpu_count())

print(datetime.date.today())
print(sys.path)
```
```
import requests # Not working, need pip

```
- Import is a package to interact with a live API
- We can make an API call to any web address using python requests packages
- **pip is a package manager to install any packages. In terminal, pip install requests**
- to make sure it is installed, in terminal: pip -V (displays the version)


import requests

 ```
requests_api = requests.get("https://www.bbc.co.uk/")
#Make sure its correct otherwise you'll get many errors

print(requests_api.status_code)
 - 200 for success
 - 404 for errors and above
 ```

 - The data is now in our local host, saved as a dictionary (Json file)
 - **Can use a for loop to pull out data with an if loop**
 - **if data == 'something we want to pull out'**
   -  **break**

 ```
print(requests_api.headers)
print(requests_api.content)
 ```

 - On bbc website, right clock on white area and open INSPECT. It should open the code behind the website


 - checking the data types
 ```
print(type(requests_api.status_code))
print(type(requests_api.headers))
print(type(requests_api.content))
 ```

### Object orientated programming, OOP

#### Four pillars of OOP
- Abstraction : Used to hide irrelevant internal functionality of the function from the user, to reduce complexity.
- Inheritance: Inheritance provides code re-usability to the program because we can use an existing class to create a new class instead of creating it from scratch. In inheritance, the child class acquires the properties and can access all the data members and functions defined in the parent class.
- Encapsulation: It is used to restrict access to methods and variables. In encapsulation, code and data are wrapped together within a single unit from being modified by accident.
- Polymorphism: Derives from Greek, "poly" means many and "morphy" mean form. By polymorphism, we understand that one task can be performed in different ways




- Step one: Create an animal.py file to create a parent class
- Step two: Create file called reptile.py to abstract data and inherit from animal.py
- Step three: Create file called snake.py 
- Step four: Create a file called python.py and this point we should be able to utilise inheritance form multiple classes, which means we would have everything available form anima class to python

- [Information from Java T point]https://www.javatpoint.com/

### Animal class 

-  follow the correct naming convention
- We need to initialise with build it method called __init__(self)
- self refers to current class
```
class Animal:       #We declare attributes in out init method
     def __init__(self):
         self.aline = True
         self.spine = True
         self.eyes = True
         self.lungs = True

     def breathe(self):
         return ("Keep brething, stay alive")

     def eat(self):
         return "Time to eat"

     def move(self):
         return "Dance"

```
- We need to create an object of this class in order to use any methods
- For cat as a user the functionality inside Animal class and the method breathe is abstracted
```
cat = Animal()
print(cat.eat())
```

### Reptile class

#### Create a Reptile class to inherit Animal class

```
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

```
- Let's create an object of Reptile class
```
smart_reptile = Reptile()

print(smart_reptile.breathe()) #breathe method is inherited from Animal class
print(smart_reptile.hunt()) # hunt() is available in Reptile class
print(smart_reptile.eat())
print(smart_reptile.move())
print(smart_reptile.hunt())
```

### Snake class

#### Create a Snake class
```
from reptile import Reptile

class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.cold_blooded = True


    def use_tongue_to_smell(self): # Adding some specific methods/behaviours
        return " *Hiss* "


smart_snake = Snake()
print(smart_snake.move()) # move() is available from Animal class
print(smart_snake.hunt())# hunt () is available from Reptile class
```
### Python class

#### Create a Python class
```
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
```