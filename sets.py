set1 = {9, 8, 7, 6}
set2 = set({"a", "b", "c", "d", "e"})
print(set1) # {8, 9, 6, 7}
print(set2) # {'a', 'c', 'b', 'e', 'd'}

set3 = set(range(1, 12, 2))
print(set3) # {1, 3, 5, 7, 9, 11}

set4 = {3, 6, 9, 12 ,15}

for i in set4:
    print(i) # 3 6 9 12 15

print(12 in set4) # True