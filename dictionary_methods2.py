ex1 = {}.fromkeys(["address"], "1600 Pennsylvania Ave NW")
print(ex1)

print("")

ex1 = {}.fromkeys("ad", "1600 Pennsylvania Ave NW")
print(ex1)

print("")

ex1 = {}.fromkeys(["brand"])
print(ex1)

print("")

ex2 = {"make": "Honda", "model": "Civic", "year": 2016}
ex2.pop("model")
print(ex2)

print("")

popped = ex2.pop("year")
print(popped)

print("")

ex3 = {"name": "bob", "age": 38, "occupation": "accountant", "workplace": "H&R Block"}
ex3.popitem()
print(ex3)

print("")


# Exercise

# use .fromkeys() to create a dictionary that has the consonants from the alphabet as its keys and the string "consonant" as the value for each of those keys.  Only use lower case letters for the consonants.  "y" counts as a consonant for this exercise.  Use a for loop and the .items() method to print each of those key: value pairs on a different line.  For example, the first 3 lines in the output should be the following:

# b consonant

# c consonant

# d consonant

# paste this dictionary into your .py file then pop and print "Big Mac" from it

# fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
# use .popitem() to remove the last key: value pair from the dictionary assigned to fast_food_items then print new fast_food_items dictionary.


var = dict.fromkeys("bcdfghjklmnpqrstvwxyz", "consonant")
for key, value in var.items():
    print(key, value)
fast_food_items = {
    "McDonald's": "Big Mac",
    "Burger King": "Whopper",
    "Chick-fil-A": "Original Chicken Sandwich",
}
print(fast_food_items.pop("McDonald's"))
print(fast_food_items)
fast_food_items.popitem()
print(fast_food_items)
