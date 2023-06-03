all_low = "there are no capitals here"
print(all_low.upper())  # THERE ARE NO CAPITALS HERE
print(all_low)
print("")

all_up = "THERE ARE NO LOWERCASE HERE"
print(all_up.lower())  # there are no lowercase here
print(all_up)
print("")

print("Mixed Case".isupper())  # False
print("ALL CAPS".isupper())  # True

print("")

print("AHHHH!".islower())  # False
print("$100 is a lot to make an hour".islower())  # True


print("")

print("Batman".isalpha())  # True
print("Batman2".isalpha())  # False

print("")

print("Batman123".isalnum())  # True
print("123".isalnum())  # True

print("")

print("123".isdecimal())  # True
print("1.23".isdecimal())  # False

print("")

print(" ".isspace())  # True
print("            ".isspace())  # True
print("not just spaces".isspace())  # False

print("")

print("The Empire Strikes Back".istitle())  # True
print("Super Smash Bros. Ultimate".istitle())  # True
print("the great gatsby".istitle())  # False

print("")

print("Hello".startswith("H"))  # True
print("Hello".startswith("h"))  # False

print("")

print("Hello".endswith("o"))  # True
print("Hello".endswith("O"))  # False

print("")

print("".join(["one", "two", "three"]))  # onetwothree
print(" ".join(["one", "two", "three"]))  # one two three
print(", ".join(["one", "two", "three"]))  # one,two,three
print(", ".join(["one", "two", "three"]))  # one, two, three
print("... ".join(["one", "two", "three"]))  # one... two... three

print("")

print(
    "Eggs, Milk, Waffles, Bacon".split(",")
)  # ['Eggs', ' Milk', ' Waffles', ' Bacon']

print("")

# * Exercise

print("Exercise")

# Create a variable called mixed_case and assign it the string "A Song of Ice and Fire"

string = "A Song of Ice and Fire"

# Use .isupper() to check if mixed_case is a string of all upper case letters.  print() the result.

print(string.isupper())

# Use .islower() to check if mixed_case is a string of all lower case letters.  print() the result.

print(string.islower())

# Change all of the letters in mixed_case to upper case letters using .upper() and print() the result.

print(string.upper())

# Change all of the letters in mixed_case to lower case letters using .lower() and print() the result.

print(string.lower())

# Use the .istitle() method to check if mixed_case is title case and print the result.

print(string.istitle())

# Create a variable called title_case and assign it the result of .title() being called on mixed_case.

title_case = string.title()

# print() title_case

print(title_case)

# Call startswith() on mixed_case with the letter mixed_case starts with as its argument.  print() the result.

print(string.startswith("A"))

# Call endswith() on mixed_case with the letter mixed_case ends with as its argument.  print() the result.

print(string.endswith("e"))

# Create a variable called words and assign it the result of split() being used on mixed_case.

words = string.split()

# print the variable "words"

print(words)

# Use the .join() method to join together all of the items in the list assigned to words as a single string.  Use .isalpha() to check if the string is made up entirely of letters.  Finally, use print() to display the result.

print("".join(words).isalpha())
