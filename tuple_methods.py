nested = (1, 2, 3, (4, 5, 6), (7, 8, 9), (10, 11, 12))
print(nested[4])  # (7, 8, 9)
print(nested[5][1])  # 11

print("")

repeat = (7, 3, 3, 3, 0, 0, 7, 0, 0)
print(repeat.count(7))  # 2
print(repeat.count(3))  # 3
print(repeat.count(0))  # 4

print("")

ints = (1, 1, 7)
print(ints.index(7))  # 2
print(ints.index(1))  # 0
# print(ints.index(8))  # ValueError: tuple.index(x): x not in tuple