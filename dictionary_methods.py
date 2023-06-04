birth_years = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
print("")
print(birth_years.keys())  # returns a list of keys

for key in birth_years.keys():
    print(key)  # returns a list of keys

print("")
print(birth_years.values())  # returns a list of values
print("")
for value in birth_years.values():
    print(value)  # returns a list of values

print("")
print(birth_years.items())  # returns a list of key value pairs
print("")
for key, value in birth_years.items():
    print(key, value)  # returns a list of key value pairs

print("")
print("elizabeth" in birth_years.values())  # returns True
print("")
if 1975 in birth_years.values():
    print(birth_years[1975])
else:
    print("1975 is not in the dictionary")

print("")
print(birth_years.get(1975, "1975 is not in the dictionary"))  # returns "1975 is not in the dictionary"

# Exercise

# create a variable and assign it the following dictionary:

# {"Queen": "Bohemian Rhapsody", "Bee Gees": "Stayin' Alive", "U2": "One", "Michael Jackson": "Billie Jean", "The Beatles": "Hey Jude", "Bob Dylan": "Like A Rolling Stone"}
# make the dictionary span multiple lines so that the line the dictionary starts on is not too long.

# print the length of the dictionary.

# use the .keys() method and a for loop to get and print all of the keys from the dictionary on separate lines.

# print all of the values from the dictionary using the .values() method.

# use .items() with a for loop to iterate through and print all of the key value pairs from the dictionary.

# use the .get() method to check the dictionary for the key

# "Promise of the Real"
# and create a message that will print if the key is not found in the dictionary.

var = {
    "Queen": "Bohemian Rhapsody",
    "Bee Gees": "Stayin' Alive",
    "U2": "One",
    "Michael Jackson": "Billie Jean",
    "The Beatles": "Hey Jude",
    "Bob Dylan": "Like A Rolling Stone",
}
print(len(var))
for key in var.keys():
    print(key)
for value in var.values():
    print(value)
for key, value in var.items():
    print(key, value)
print(var.get("Promise of the Real", "Key not found"))
