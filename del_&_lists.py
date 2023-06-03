planets = ["pluto", "mars", "earth", "venus"]

# del planets[0]
# print(planets) # ['mars', 'earth', 'venus']

planets.remove("pluto")
print(planets)  # ['mars', 'earth', 'venus']

colors = ["blue", "red", "white", "blue", "orange", "blue"]
colors.remove("blue")
print(colors)  # ['red', 'white', 'blue', 'orange', 'blue']

pets = ["cat", "dog", "parrot"]
print(pets)
pets.append("fish")  # add to end
print(pets)

pets.insert(1, "bird")  # add to index 1
print(pets)

list = [2.718, 4, -19, 1000, 0]
print(list)  # [2.718, 4, -19, 1000, 0]
list.sort()  # sort in place
print(list)  # [-19, 0, 2.718, 4, 1000]
list.sort(reverse=True)  # sort in place
print(list)  # [1000, 4, 2.718, 0, -19]

mixed = [False, 5.67, "string", -2]
# mixed.sort()  # TypeError: '<' not supported between instances of 'str' and 'bool'

ASCII = ["Andy", "kiwi", "apple", "Karen", "Brian", "banana"]
ASCII.sort(key=str.lower)  # sort in place
print(ASCII)  # ['Andy', 'Brian', 'Karen', 'apple', 'banana', 'kiwi']

metals = ["copper", "gold", "silver", "iron"]
print(metals.index("silver"))  # 2

bands = ["Queen", "Led Zepplin", "The Beatles", "Muse", "Radiohead"]
end = bands.pop()  # remove last element
print(end)  # Radiohead

# Exercise

# Create a variable called arctic_animals and assign it the list ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]

var = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]

# Use del to remove "tiger" from the list assigned to arctic_animals.

del var[4]

# Use the .remove() method to remove the string "elephant" from the list assigned to arctic_animals.

var.remove("elephant")

# Use the .append() method to add the string "arctic fox" to the list arctic_animals.

var.append("arctic fox")

# Use .insert() to insert the string "snowy owl" between the strings "polar bear" and "walrus" inside of arctic_animals.

var.insert(3, "snowy owl")

# Use the .sort() method to rearrange the strings in arctic_animals into alphabetical order.

var.sort()

# Use print() to display the list assigned to arctic_animals

print(var)

# Use .index() to get the index number of "reindeer" from arctic_animals then print it.

print(var.index("reindeer"))

# Use .pop() to get the last item from the list arctic_animals then print it.

print(var.pop())
