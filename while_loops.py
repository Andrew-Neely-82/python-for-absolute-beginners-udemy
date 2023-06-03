counter = 0

while counter < 5:
    print("Something")
    counter += 1

# Exercise

# For this exercise, you will print 10 descending integers starting from 10 and ending at 1 with each integer being 1 less than the last and each integer printed on a new line.

# Create a variable and assign it the integer 10.

# Then, print

# 10

# 9

# 8

# 7

# 6

# 5

# 4

# 3

# 2

# 1

# in the output by using a while loop to print numbers while the variable does not equal 0.  Use the -= operator to reassign descending values to the variable.

var = 10

while var > 0:
    print(var)
    var -= 1


# Exrercise 2

# Write a program which gets a positive integer from a user using input() and assigns it to a variable.

# The program should then use a while loop to get the sum of all of the integers from the integer that was entered by the user down to 1.  For example, if the integer entered by the user was 6, the while loop would find the sum of 6, 5, 4, 3, 2, and 1, which is 21.

# At the bottom of your program create two print statements.  One will display the user entered integer and the other will display the sum found by the while loop.

pos_int = int(input("Please enter a positive integer: "))
int_init = pos_int
summed = 0
while pos_int > 0:
    summed += pos_int
    pos_int -= 1

print(int_init)  # displays the initial value of pos_int
print(summed)  # displays the sum of integers from pos_int
