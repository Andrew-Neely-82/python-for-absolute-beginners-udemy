def print_four():
    print("this")
    print("is")
    print("a")
    print("function")


print_four()

print("")
print("")
print("")


def add(a, b):
    return a + b


print(add(1, 2))


print("")
print("Default Values function: ")


def example(num1=2, num2=3):
    print(num1 + num2)


example(5, 2)

# print("")
# print("Return function: ")

# def add_return(a=7, b=8):
#   return a + b

# print(add())

# print("")
# print("Return function with expressions: ")

# print(add_return() + 44) # this will not work because the function is not returning anything


# * Exercise 1

# Create a function called hello_world_printer() which takes no parameters and prints the string "hello world"

print("")
print("Exercise 1: ")


def hello_world_printer():
    print("hello world")


# Call the function hello_world_printer()

hello_world_printer()

# * Exercise 2

print("")
print("Exercise 2: ")

# Create a function called name_printer which takes 1 parameter and prints it


def name_printer(name):
    print(name)


# Create a variable called name and assign it user input().  input()'s message should ask the user to enter their name.

name = input("Enter your name: ")

# Call name_printer() with the variable "name" as its argument.

name_printer(name)

# Exercise 3

print("")
print("Exercise 3: ")

# For this programming challenge, you will be creating a function that calculates the volume of a rectangular prism in cubic feet.  The formula to find the volume of a rectangular prism is V = l * w * h where l, w, and h are length, width, and height, respectively.

# First, create three variables representing length, width, and height.   Assign each of them an integer as user input using the input() function and int().

length = int(input("Enter length: "))
width = int(input("Enter width: "))
height = int(input("Enter height: "))

# Next, create a function to calculate the volume of the rectangular prism.  It should have 3 parameters representing length, width, and height and return the volume of a rectangular prism calculated using those 3 parameters.


def volume(length, width, height):
    return length * width * height


# Finally, use print() to display "The volume of the rectangular prism is [call function  here to calculate volume] cubic feet." in the output.  You will have to use str() on the function call to be able to concatenate it with strings since it returns an integer.

print(
    "The volume of the rectangular prism is "
    + str(volume(length, width, height))
    + " cubic feet."
)

# Exercise 4

print("")
print("Exercise 4: ")

# The formula for converting from degrees Celsius to degrees Fahrenheit is as follows:

# F = 1.8 * C + 32

# Where F is the Fahrenheit temperature and C is the Celsius temperature.

# In a .py file, create a variable and assign it an integer representing a celsius temperature that is entered as user input().  input()'s message should prompt the user to enter an integer value.

# For this programming challenge, you will then write a function called fahrenheit that takes in an integer representing a Celsius temperature as its argument.  The function will return the Fahrenheit equivalent temperature of that argument to 1 place after the decimal.

# At the end of your program, display the Fahrenheit equivalent in a print statement message formatted like so:  "The Fahrenheit equivalent of [user entered integer] degrees Celsius is [number returned by function]".

# To make sure that the function works, run your program multiple times and call the function on different user entered integer values both negative and positive.

celsius = int(input("Please enter an integer value for degrees celsius. "))


def fahrenheit(cel):
    return (18 * cel + 320) / 10


print(
    "The Fahrenheit equivalent of "
    + str(celsius)
    + " degrees Celsius is "
    + str(fahrenheit(celsius))
    + "."
)
