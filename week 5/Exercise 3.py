'''Write a program that takes a bunch of command-line arguments, and then prints
out the shortest. If there is more than one of the shortest length, any will do.'''

import sys

if len(sys.argv) == 1:
    print("No arguments were provided.")
else:
    shortest = min(sys.argv[1:], key=len)
    print(f"The shortest argument is: {shortest}")
