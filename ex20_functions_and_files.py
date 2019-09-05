# Filese and functions

from sys import argv
# passing script and input_file as arguments to python script execution from cmd
script, input_file = argv

# prints input file contents
def print_all(f):
	print(f.read())
	
# takes python interpretor to beginning of the file
def rewind(f):
	f.seek(0)
	
# prints a single line
def print_a_line(line_count, f):
	print(line_count, f.readline())

# setting current file variable	
current_file = open(input_file)

print("Let us first print the whole file:\n")

# prints all contents of input file
print_all(current_file)

# takes interpretor to beginning of the input file
rewind(current_file)

print("Let's print three lines")

# Prints first line
current_line = 1
print_a_line(current_line, current_file)

# Prints second line of file
current_line += 1
print_a_line(current_line, current_file)

# Prints third line of file
current_line += 1
print_a_line(current_line, current_file)
