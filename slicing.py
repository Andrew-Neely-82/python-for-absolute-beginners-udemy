example = ["carptet", "hardwood", "linoleum"]

print(example[1])  # hardwood

example2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(example2[2][0])  # 7

# negative indexing

negative_list = [1, 2, 3, 4, 5]

print(negative_list[-1])  # 5

mixed = [False, 365, 4.24, "this is a string"]
print(mixed[2] + 1.76)
print('i have used "' + mixed[-1] + '" as an example too many times')


sliced = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sliced[:4])  # from the beginning to 4
print(sliced[3:8])  # from 4 to 8
print(sliced[6:])  # from 7 to the end

example3 = [2, 4, 6, 8, 0]
print(example3)  # [2, 4, 6, 8, 0]
example3[3] = 10
print(example3)  # [2, 4, 6, 10, 0]
example3[4:7] = [7, 6, 5]
print(example3)  # [2, 4, 6, 10, 7, 6, 5]

print("")

# * Exercise

# Create a variable and assign it the list [[0, 2], [4, 6], [8, 10], [12, 14]]

# Access the first list from the list of lists in step 1 by index then print it.

# Access the 14 from the list in step 1 then print it.

# Create a second variable and assign it the list ["chair", "table", "desk", "lamp", "bed"]

# Use a negative integer to access "chair" from the variable in step 4 by index then print it.

# Print "Most people own at least 2 chairs." by concatenating the 2 from the list in step 1 and the "chair" from the list in step 4 with "Most people own at least ", a space, and a period.

# Create a third variable and assign it the list [0.98, 8.76, 6.54, 4.32]

# Print the slice [8.76, 6.54, 4.32] from the variable you created in step 7.

# Print the slice [8.76, 6.54] from the variable you created in step 7.

# Print the slice [0.98, 8.76] from the variable you created in step 7.

var = [[0, 2], [4, 6], [8, 10], [12, 14]]
print(var[0])
print(var[3][1])
var2 = ["chair", "table", "desk", "lamp", "bed"]
print(var2[-5])
print("Most people own at least " + str(var[0][1]) + " " + var2[0] + "s.")
var3 = [0.98, 8.76, 6.54, 4.32]
print(var3[1:])
print(var3[1:3])
print(var3[:2])
