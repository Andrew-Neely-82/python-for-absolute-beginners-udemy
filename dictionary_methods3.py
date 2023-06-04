ex1 = {1: "England", 2: "Scotland", 3: "Wales", 4: "Northern Ireland"}
print(ex1)
ex1.clear()
print(ex1)

print("")

birth_years = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
print(birth_years)
people = birth_years
people[1982] = "madeleine"
print(birth_years)

print("")

city_info = {"county": "Canada", "province": "Ontario", "city": "Toronto"}
print(city_info)
population = {"population": 2930000}
city_info.update(population)
print(city_info)

print("")

# Exercise

# paste these 2 dictionaries into your file

# internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
# another_one = {"shroud": "Twitch"}
# use .update() to add the contents of another_one to internet_celebrities.

# create a variable and assign it a copy of internet_celebrities.

# use the .clear() method to get rid of the contents of internet celebrities.

# print internet_celebrities.

# print the variable you created in step 3.

internet_celebrities = {
    "DrDisrespect": "YouTube",
    "ZLaner": "Facebook",
    "Ninja": "Mixer",
}
another_one = {"shroud": "Twitch"}
internet_celebrities.update(another_one)
var = internet_celebrities.copy()
internet_celebrities.clear()
print(internet_celebrities)
print(var)
