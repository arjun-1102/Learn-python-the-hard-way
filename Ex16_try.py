from sys import argv

script, filename = argv

# # Opening the file for read
fileops = open(filename)

# # reading and storing contents in temp variable - which is an object
temp = fileops.read()
fileops.close()


# Reopening file for write
fileops_two = open(filename, 'w')
# truncating the file - erasing all contents of hte file
fileops_two.truncate()
# Adding text at the beginning of the file
fileops_two.write("This is the text i've entered.\n")
fileops_two.write(temp)
fileops_two.close()

fileops_three = open(filename)
print(fileops_three.read())
fileops_three.close()