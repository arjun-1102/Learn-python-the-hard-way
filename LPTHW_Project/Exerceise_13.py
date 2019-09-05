# ## ## ## ##---- Exercise 13: Parameters, Unpacking and variables
from sys import argv
script, second = argv
# print("This script is called", sys.argv[0])
# print("It's length is", len(sys.argv))
# print("Names of variables", str(sys.argv))

print("This script is called", argv[0])
print("It has %r variables" % len(argv))
