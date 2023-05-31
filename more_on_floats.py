print(1.23 + 2.80)

ex2 = (123 + 280) / 100
print(ex2)

# round() function

ex3 = 1.23 + 2.80
print(round(ex3, 2))

summed = 3.14159 + 2.71828
print(round(summed, 4))

# Programming Challenge: Grocery Store Purchase
# A customer of a grocery store is purchasing 6 items. The names and prices of the items are as follows:

# Penne 16 oz Pack of 12 - $16.68

# Arrabiata Pasta Sauce 24 oz - $6.98

# Bag of 20 Organic Garlic Cloves - $16.78

# Italian Seasoning 1.5 oz Bottle - $15.26

# Artisan Baguettes Twin Pack - $3.00

# 12 oz Bag of Meatballs - $4.39

# In a .py file, write a program which calculates the subtotal of all 6 of these items using an expression.  The subtotal is just the sum of all of their prices.

penne = 16.68
sauce = 6.98
garlic = 16.78
seasoning = 15.26
baguettes = 3.00
meatballs = 4.39

subtotal = penne + sauce + garlic + seasoning + baguettes + meatballs
print(round(subtotal, 2))
