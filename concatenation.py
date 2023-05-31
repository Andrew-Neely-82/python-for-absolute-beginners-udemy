nut = "walnut"
fruit = "banana"
print(nut + " " + fruit)

concatenated = nut + " " + fruit
print(concatenated)  # makes walnut banana
print(concatenated[3])  # makes n
print(concatenated[1:4])  # makes aln

unchanged = "forrest gump"
sliced = unchanged[6:]
print(sliced)  # makes gump
print(unchanged[10])  # makes m
print(unchanged)  # makes forrest gump

print("=====================================")
print("=====================================")
print("=====================================")

# Do all of this in a .py file in Pycharm
print("")
print("Exercise")
print("")

# Create a variable and assign it the string "Just do it!"
word = "Just do it!"

# Access the "!" from the variable by index and print() it
print('Access the "!" from the variable by index and print() it', word[10])

# Print the slice "do" from the variable
print('Print the slice "do" from the variable :', word[5:7])

# Get and print the slice "it!" from the variable
print('Get and print the slice "it!" from the variable :', word[8:])

# Print the slice "Just" from the variable
print('Print the slice "Just" from the variable :', word[:4])

# Get the string slice "do it!" from the variable and concatenate it with the string "Don't ".  Print the resulting string, which should be "Don't do it!" where the "do it!" part is a slice.
print(
    'Get the string slice "do it!" from the variable and concatenate it with the string "Dont ".'
)
print("Don't " + word[5:])
