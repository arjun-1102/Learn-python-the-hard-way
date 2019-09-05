from sys import argv
# Define input arguments
script, file_name = argv
# open the file with specified name
txt = open(file_name)
# Print out the file name
print(f"Here's your file {file_name}:")
# Print the text of the file
print(txt.read())
# Prompt for input 
print("Type the file name again")
file_again = input(">")
# Open file again
txt_again = open(file_again)
# Print text inside file
print(txt_again.read())

