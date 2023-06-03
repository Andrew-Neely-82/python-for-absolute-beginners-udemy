one_input = range(5)  # start at 0, stop at 5, step is 1

for num in one_input:
    print(num)

print("")

three_inputs = range(1, 20, 3)  # start, stop, step

for num in three_inputs:
    print(num)  # prints 1, 4, 7, 10, 13, 16, 19

print("")

# Exercise

# Write a program that iterates over the integers 1 through 50 using a loop.

# However, for numbers which are multiples of both 3 and 5 print “FizzBuzz” in the output.  For example, 15 is divisible by both 3 and 5, so instead of printing 15, print "FizzBuzz".  For numbers which are multiples of 3 but not 5 (such as 42) print “Fizz” instead of the number.  For the numbers that are multiples of 5 but not 3 (such as 20) print “Buzz” instead of the number.

# All of the integers which are not multiples of 3 or 5 should just be printed as themselves.

for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz ")
    else:
        print(num)

print("")


# Challenge

# Create a function which takes one positive integer as its input and returns its factorial.

# To make sure that your function works correctly, you should call it with the inputs 3, 4, and 5 and print what is returned by those calls.  For those inputs, you should get 6, 24, and 120, respectively.


def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(3))
print(factorial(4))
print(factorial(5))
