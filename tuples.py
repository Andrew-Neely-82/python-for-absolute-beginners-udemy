# Tuples are immutable sequences of arbitrary objects.

tuple1 = ("a", "b", "c", "d", "e")
tuple2 = (2.718, False, [1, 2, 3])
tuple3 = (1, 1, 0, 0, 0)
tuple4 = (5, 4, 3, 2, 1)
tuple5 = tuple([3.14, 2.205, 10])
tuple6 = tuple("ebcba")
print(tuple5)  # (3.14, 2.205, 10)
print(tuple6)  # ('e', 'b', 'c', 'b', 'a')

tuple7 = tuple({"a": 1, "b": 2, "c": 3})
print(tuple7)  # ('a', 'b', 'c')

tuple8 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tuple8[3])  # 4
