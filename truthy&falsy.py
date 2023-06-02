example = input("Enter any string other than a blank string: ")

if example != "":
    print("You entered something.")
else:
    print("You did not enter a string.")


print(bool(0))  # False
print(bool(3.14))  # True
print(bool("false"))  # True
