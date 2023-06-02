import random


num = int(input("Please enter a integer : "))

if num < 0:
    print("The number is negative")
elif num == 0:
    print("The number is zero")
elif 0 > num <= 100:
    print("The number is between 0 and 100")
else:
    print("The number is positive")

# Exercise

# For this exercise, start by creating a variable and assigning it a randomly generated integer between and inclusive of both 1 and 10.

# Then, using your knowledge of if, elif, and else statements, create a program which prints the roman numeral equivalent of the randomly generated number.

# For example, if the randomly generated integer was 9, then the program would say that the roman numeral equivalent of 9 is IX in the output.

var = random.randint(1, 10)

if var == 1:
    print("The roman numeral equivalent of " + str(var) + " is I.")
elif var == 2:
    print("The roman numeral equivalent of " + str(var) + " is II.")
elif var == 3:
    print("The roman numeral equivalent of " + str(var) + " is III.")
elif var == 4:
    print("The roman numeral equivalent of " + str(var) + " is IV.")
elif var == 5:
    print("The roman numeral equivalent of " + str(var) + " is V.")
elif var == 6:
    print("The roman numeral equivalent of " + str(var) + " is VI.")
elif var == 7:
    print("The roman numeral equivalent of " + str(var) + " is VII.")
elif var == 8:
    print("The roman numeral equivalent of " + str(var) + " is VIII.")
elif var == 9:
    print("The roman numeral equivalent of " + str(var) + " is IX.")
else:
    print("The roman numeral equivalent of " + str(var) + " is X.")
