import sys

# make the type input before enter to being a list and print the element
# try:
#     print("My name is", sys.argv[1])
# except IndexError:
#     print("Lack of argument")

if len(sys.argv) < 2:
    sys.exit("To few argument")
# elif len(sys.argv) > 2:
#     sys.exit("To many argument")

# get all argument, slice start from index 1 not 0, end for -1 index
for arg in sys.argv[1:-1]:
    print("My name is", arg)