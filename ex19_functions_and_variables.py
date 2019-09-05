# Functions and Variables

# Defining the main function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"You have {cheese_count} cheeses!")
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	print("Man that's enought for a party")
	print("Get a blanket")


# Calling the function using direct argument values	
print("We can just give the function numbers directly")
cheese_and_crackers(20,30)

# Calling the function using variable names from script
print("Or, we can use variables from our script")
amount_of_cheese = 20
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Calling the function with math funcitons in arguments
print("We can even do math inside")
cheese_and_crackers(10+20, 4+2)

# Calling the function with math functions in arguments
print("And we can combine the two")
cheese_and_crackers(10+amount_of_cheese, 4+amount_of_crackers)

