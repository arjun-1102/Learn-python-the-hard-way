# ## ## ## ##---- Exercise 12 : Prompting input


age_one = input("How old are you?")
height_one = input("How tall are you?")
weight_one = input("How much do you weigh?")

# Python 2
# print("So you're %r old, %r tall and %r heavy!" % (age_one, height_one, weight_one))

# Python 3
print(f"So, you're {age_one} old, {height_one} tall and {weight_one} heavy!")