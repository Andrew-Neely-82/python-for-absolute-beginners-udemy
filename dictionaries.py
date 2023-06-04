consoles = {"nintendo": "wii", "microsoft": "xbox", "sony": "playstation"}

print(consoles["microsoft"])  # xbox
val = consoles["microsoft"]
print(val)  # xbox
print(
    "The " + consoles["sony"] + " 5 is Sony's newest gaming console"
)  # The playstation 5 is Sony's newest gaming console

mohs = {9: "corundum", 10: "diamond"}
floats = {1.23: 1000, 3.14: 10000, 2.71: 100000}
mixed = {"string": 1, 10210: 2, 4.976: 3, False: 4}


# Exercise

# create a variable and assign it a dictionary that has 5 key value pairs

# print and access the value held at the third key in the dictionary

# use the in keyword to check if a key appears in the dictionary and print the result

# use not in to check if a key does not appear in the dictionary and print the result

var = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}
print(var["key3"])
print("key3" in var)
print("key3" not in var)
