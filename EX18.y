# Names, variables, Code, Functions

# functions do three things:
# 1. They name pieces of code(like variables name strings/integers)
# 2. They take arguments(like script takes argv)
# 3. Using 1 & 2, they allow you to make mini scripts

# this one is like your script with argv
def print_two(*args):
	arg1, arg2 = args
	print(f"arg1 : {arg1}, arg2 : {arg2})
	
# *args is pointless, improvisation
def print_two_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2})
	
# this just takes one arguments
def print_one(arg_one):
	print(f"arg1: {arg_one}")
	
# This one does not take any arguments
def print_none():
	print("I got nothing")
	
print_two("Arjun", "Sharma")
print_two_again("Arjunone","SharmaOne")
print_one("First")
print_none()