name = input("Please enter your name: ")
print("Your name is " + name + ".")
print(type(name))

# converts var to string

# In a .py file, create a program and use input() three times to get answers to the following questions from a user.  Store each of the answers in a variable.

input("What is your name? ")

# What is your name?

name = input("What is your name? ")

# What is your quest?

quest = input("What is your quest? ")

# What is your favorite color?

color = input("What is your favorite color? ")

# Then, concatenate everything into a string within a print() statement with the form "So your name is [name], your quest is [quest], and your favorite color is [color]."

print(
    "So your name is "
    + name
    + ", your quest is "
    + quest
    + ", and your favorite color is "
    + color
    + "."
)
