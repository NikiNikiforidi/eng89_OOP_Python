# ## Modules packages and files in python
# **Pythons extensive documentation on python.org
# - IMPORT is the keyword used to Import and modules available

# ### Math

# import math
# import random #Generates random number
# num1 = 23.44
#
# # - Real life situation you have to round the figure depending on the value.
# # - If the value is less than .50 round it down 23.0, if 23.51 then round it up.
#
# print(math.ceil(num1)) #Rounds up to 24
# print(math.floor(num1)) #Round down to 23
#
# # - Random call/methods
#
# print(random.random()) #Number changes everytime you run between .0-.99
#
# print(math.pi)
#
#
# # - Another way to add library
# from random import random
# print(random()) #Don't need to use '.random'


# Let's see how to interact with our machine using python import os
import math

# import datetime
# import os
# import sys # sys is used to get system specifications
#
# work_dir = os.getcwd() # provides the currently location/path
# print(work_dir)
#
#
# # - linux/Mac
# # print(os.getuid())
# # print(os.uname())
# # print(os.cpu_count())
#
# print(datetime.date.today())
# print(sys.path)

import requests # Not working, need pip
# - Import is a package to interact with a live API
# - We can make an API call to any web address using python requests packages
# - pip is a package manager to install any packages. In terminal, pip install requests
# to make sure it is installed, in terminal: pip -V (displays the version)


#
# import requests
#
# # ```
# requests_api = requests.get("https://www.bbc.co.uk/")
# #Make sure its correct otherwise you'll get many errors
#
# print(requests_api.status_code)
# # - 200 for success
# # - 404 for errors and above
# # ```
#
# # - The data is now in our local host, saved as a dictionary (Json file)
# # - **Can use a for loop to pull out data with an if loop**
# # -**if data == 'something we want to pull out'
# #   -         break**
#
# # ```
# print(requests_api.headers)
# print(requests_api.content)
# # ```
#
# # - On bbc website, right clock on white area and open INSPECT. It should open the code behind the website
#
#
# # - checking the data types
# # ```
# print(type(requests_api.status_code))
# print(type(requests_api.headers))
# print(type(requests_api.content))
# # ```

# ### Object orientated programming, OOP

# #### Four pillars of OOP
# - Abstraction
# - Inheritance
# - Encapsulation
# - Polymorphism

# - Step one: Create an animal.py file to create a parent class
# - Step two: Create file called reptile.py to abstract data and inherit from animal.py
# - Step three: Create file called snake.py
#- Step four: Create a file called python.py and this point we should be abole to ultilise inheritance form multiple classes, which means we woyld have everything availabe form anila class to python



