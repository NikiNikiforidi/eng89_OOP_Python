# # ## Functions
# # - Syntax def is used to declare followed by the name of the function()
#
#
# # #### First iteration, using PRINT
# def greeting():
#     print("Welcome and enjoy the trip!")
# #pass # Pass = keyword. Allows interpreter to skip without causing errors
#
#
# # - To use a function you need to 'call' it.
# # - Once called, everything in the function will be interpreted
# greeting ()
# print (greeting())
#
#
#
# # #### Second iteration, using RETURN
# def greeting():
#     print("Kalimera")  # Goodmorning in Greek
#     return "Welcome and enjoy your trip!"
#
# print(greeting())



# # #### Third iteration, with user name as str and arguments
# def greeting(name):  # The argument is what is inside the brackets
#     return "Welcome on board " + name.title()
#
# print(greeting("niki"))

# **TASK: Create a function to prompt a user to enter name and display back with greeting**


# def greeting(name):
#     return f"Welcome {name.title()}!! I am a greeting message..."
#
# # print(greeting(input("Please enter your name: ")))
#
# # -Teachers version:
#
# user_name = input ("Please enter your name: ")
# def greeting (name):
#     return "Welcome on board " + name
#
# print( greeting(user_name))



# - Lets create a function with multiple argum.
def add(num1, num2):
    return num1 + num2

print(add(1,2))



# - Order inside function matters, RETURN goes last
def multiply(num1,num2):
    return num1 * num2
    print("This function multiplies 2 numbers")
print(multiply(3,3))


def multiply(num1,num2):
    print("This function multiplies 2 numbers")
    return num1 * num2
print(multiply(3,3))

