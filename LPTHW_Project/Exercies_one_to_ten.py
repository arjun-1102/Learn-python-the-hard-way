# ## Exerciese 2 : Commenting
# This is just a test
#
# Can multiple lines be commented/uncommented using this shortcut
# cltr + /
# The answer is: Yes

# #--- Playing with numbers

# ## Mathematical operations in python ->
# # + - * / %

# # Logical operations in python ->
# # < >  <= >= ==

# # ## ## ## #---- Exercise 3 : Counting chicken
# I will now count my chicken:
# Hens 30
# Roosters 97
# Now I will count the eggs:
# 7
# Is it true that 3 + 2 < 5 - 7 ?
# False
# What is 3 + 2 ? 5
# What is 5 - 7 ? -2
# That is why it is false
# Is it greater? True
# Is it greater or equal ? True
# Is it less or equal ? False

# # ## ## ## #---- Exercise 4 : Variable and names
# #-- General advise : Keep variable names relevant, long variable names may not be a problem

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can trasnport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car")

# ## ## ## ##---- Exercise 5 : More variables and printing
# When printing : %s - string
#                     %d - float
#                     %r - print everything no specific data type
# %s,%d,%r are called formatters -  Used in the format : String(with %s,%d,%r) % (variable names/list)





my_name = 'Zed A Shaw'
my_age = 35  # not a lie
my_height = 74  # inches
my_weight = 180  # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print("Let's talk about %s" % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy" % my_weight)
print("Actually that's not too heavy")
print("He's got %s eyes and %s hair" % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee" % my_teeth)

# ## Advanced printing
print("If I add %d, %d and %d, I get %d" % (my_age,
                                           my_height,
                                           my_weight,
                                           my_age + my_height + my_weight))

# ##---- Testing

# # Q. Convert 100 miles to km

dist_miles = 100
conversion_factor_dist = 0.6213
dist_km = round(dist_miles / conversion_factor_dist, 2)
print("%r miles is %r kilometers" % (dist_miles, dist_km))

# ## ## ## ##---- Exercise 6 : Strings and text
# Strings - can be put in single or double quotes ' ' = " "

# # Stores 'There are 10 types of people' into x
x = "There are %d types of people" % 10

# # Stores 'binary' into binary
binary = "binary"
do_not = "don't"

# # Stores 'Those who know binary and those who don't' into y
y = "Those who know %s and those who %s" % (binary, do_not)


print(x)
print(y)
# # %r - prints x with ''
print("I said : %r" % x)
# # %s - prints x as part of string(no '')
print("I also said : %s" % y)
# # %r - prints x with ''
print("I said : '%r'" % x)
# # %s - prints x as part of string(no '')
print("I also said : '%s'" % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# # Shows how %r at the end can be used to pass variable as string
print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side"

# No whitespace in print - concatenate without space
print(w + e)

# # Whitespace in print - concatenate with space
print(w, e)

# ## ## ## ##---- Exercise 7 : More printing
print("Mary had a little lamb.")
print("Its fleece was white as %s." % 'snow')
print("And everywhere that Mary went")
print('.' * 10)  # Prints . 10 times

# ## ## ## ##---- Exercise 8 : Printing
formatter = "%r %r %r %r"

print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
    "I had this thing",
    "That you could type up right.",
    "But it didn't sing",
    "So I said goodnight"
))

# ## ## ## ##---- Exercise 9 : Printing, printing, printing
# # -- \n prints text in the next line
# # Anything between triple """ Text here """ is printed as is in the form of paragraph
# # - \n does not work with %r

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec"

print("Here are the days: ", days)
print("Here are the months", months)
print("""There's something going on here.
With three double quotes.
We'll be able to type as much as we like
Even 4 lines if we want, or 5 or 6""")

# ## ## ## ##---- Exercise 10 : Escape characters
# Escape characters allow python to understand whether " represents end of string or is part of string to be printed

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# Escape characters work when inside """<Text here>"""

# infinite loop - caution
# while True:
#     for i in ["/", "- ", "|", "\\", "|"]:
#         print("%s\r" % i,)
