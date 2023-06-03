cities = ("Tokyo", "London", "New York", "Shanghai", "Sydney")

for city in cities:
    print(city)

print("")

count = 0
while count < len(cities):
    print(cities[count])
    count += 1

print("")

backwards = len(cities) - 1
while backwards >= 0:
    print(cities[backwards])
    backwards -= 1

ints = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(ints[::3])  # (1, 4, 7, 10)
print(ints[1::2])  # (2, 4, 6, 8, 10)
print(ints[7::-1])  # (8, 7, 6, 5, 4, 3, 2, 1)
print(ints[8::-2])  # (9, 7, 5, 3, 1)