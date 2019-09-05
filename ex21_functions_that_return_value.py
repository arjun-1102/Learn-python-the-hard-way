# Functions that return something

def add(a, b):
	print(f"Adding a + b")
	return(a+b)
	
def subtract(a, b):
	print(f"Subtracting a - b")
	return(a-b)
	
def multiply(a, b):
	print(f"Multiplying a * b")
	return(a*b)

def divide(a, b):
	print(f"Dividing a / b")
	return(a/b)
	
print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(89, 4)
weight = multiply(30, 3)
iq = divide(100, 2)

print(f"Age: {age}, height : {height}, weight: {weight}, iq: {iq}")

# A puzzle for the extra credit, type it anyway
print("Here's the puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print("What becomes ", what, "Can you do it by hand?")



