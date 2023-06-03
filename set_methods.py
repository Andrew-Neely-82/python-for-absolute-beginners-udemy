scifi = {"start trek", "star wars", "halo"}
scifi.add("mass effect")
print(scifi)

fruits = {"apple", "orange", "banana", "tomato"}
fruits.remove("tomato")
print(fruits)

fruits2 = {"apple", "orange", "banana", "tomato"}
fruits2.discard("apple")
print(fruits2)

mountains = {"Everest", "Kilimanjaro", "Fuji"}
print(mountains)
mountains.clear()
print(mountains)

mountains2 = {"Everest", "Kilimanjaro", "Fuji"}
set2 = mountains2.copy()  # or set2 = set(mountains2)
print(set2 is mountains2)  # False
print(set2)  # {'Fuji', 'Kilimanjaro', 'Everest'}

ex1 = {1, 2, 3, 4, 5}
ex2 = {6, 7, 8, 9, 10}
ex3 = ex1.union(ex2)  # or ex3 = ex1 | ex2
print(ex3)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


ex_1 = {4, 5, 6, 7, 8}
ex_2 = {6, 7, 8, 9, 10}
ex_4 = ex_1.intersection(ex_2)  # or ex4 = ex1 & ex2
print(ex_4)  # {6, 7, 8}
ex_5 = ex_1.difference(ex_2)  # or ex5 = ex1.difference(ex2)
print(ex_5)  # {4, 5}
