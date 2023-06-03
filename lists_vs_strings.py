ex1 = [1, 2, 3]
ex1[1] = 5
print(ex1)  # [1, 5, 3]

print("")

ex2 = "123"
# ex2[1] = "5"
# print(ex2)  # TypeError: 'str' object does not support item assignment

print("")

ex3 = "No, you can't!"
ex4 = "Yes" + ex3[3:11] + "!"
print(ex4)  # Yes you can!

print("")

ex5 = 3.14
ex6 = "coconut"
ex7 = ex5
ex8 = ex6
print(ex7)  # 3.14
print(ex8)  # coconut

print("")

ex9 = [1, 2, 3, 4, 5]
ex10 = ex9
ex10[2] = 4
print(ex9)  # [1, 2, 4, 4, 5]
print(ex10)  # [1, 2, 4, 4, 5]

print("")

import copy

ex12 = [1, 2, 3, 4, 5]
ex13 = copy.deepcopy(ex12)
ex13[2] = 4
print(ex12)  # [1, 2, 3, 4, 5]
print(ex13)  # [1, 2, 4, 4, 5]

ex15 = [
    "bush",
    "fern",
    "tree",
    "moss",
]  # list of strings vertically aligned will be printed as a list

print(ex15)

ex16 = 2 + \
       4 + \
       1 # line continuation character (\) is used to break a long line into multiple lines
print(ex16)  # 7
