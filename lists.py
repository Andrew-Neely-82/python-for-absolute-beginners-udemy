list1 = [5, 4, 3, 2, 1]
list2 = ["blue", "green", "red", "yellow", "orange"]
list3 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

print(list("blah"))  # ['b', 'l', 'a', 'h']

checked_list = [1, 2, 3, 4]
print(1 in checked_list)  # True
print(5 in checked_list)  # False
print(5 not in checked_list)  # True

# Exercise

# Create a variable and assign it a list that contains an integer, a float, a Boolean value, a string, and a list of 3 integers.

# Create another variable and assign it a call of the list() function with a string as its argument.

# Use the keyword "in" to check if the letter "e" is in the list assigned to the variable from step 2 and print the result.

# Use the keyword "not in" to check if the letter "a" is not in the list assigned to the variable from step 2 and print the result.

var = [1, 1.1, True, "string", [1, 2, 3]]
print(var)

var2 = list("string")
print(var2)

print("e" in var2)
print("a" not in var2)
