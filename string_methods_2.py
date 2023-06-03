print("hello world".rjust(15))  # right justify with 15 spaces
print("hello world".rjust(15, "-"))  # right justify with 15 dashes
print("hello world".ljust(15, "*"))  # left justify with 15 stars
print("hello world".center(15, ":"))  # center justify with 15 spaces
print("hello world".center(15, ":"))  # center justify with 15 spaces and 7 characters
print(
    " I had a exciting trip!!!11111".strip("1")
)  # remove whitespace from the beginning and end
print(
    "I had a exciting trip!!!11111".lstrip("1")
)  # remove whitespace from the beginning
print("I had a exciting trip!!!11111".rstrip("1"))  # remove whitespace from the end
print("hello world".replace("world", "everyone"))  # replace world with everyone

print("")

# * Exercise

# Create a variable called the_string and assign it the string "North Dakota".

the_string = "North Dakota"

# Call .rjust() on the_string with 17 as its argument and print() the result.

print(the_string.rjust(17))

# Call .ljust() on the_string with the arguments 17 and "*" then print() the result.

print(the_string.ljust(17, "*"))

# Create a variable called center_plus and assign it the result of .center() being called on the_string with 16 and "+" as arguments.

center_plus = the_string.center(16, "+")

# Use print() to display the string assigned to center_plus.

print(center_plus)

# Call .lstrip() on the_string to remove "North" then print() the result.

print(the_string.lstrip("North"))

# Call .rstrip() on center_plus with "+" as its argument and print() the result.

print(center_plus.rstrip("+"))

# Call .strip() on center_plus with "+" as its argument and print() the result.

print(center_plus.strip("+"))

# Call .replace() on the_string and replace "North" with "South".  print() the result.

print(the_string.replace("North", "South"))
