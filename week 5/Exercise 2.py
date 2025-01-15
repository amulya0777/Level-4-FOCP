'''Write a program that, when run from the command line, reports how many
arguments were provided. (Remember that the program name itself is not an
argument).
'''

import sys

if len(sys.argv) == 1:
    print("No arguments were provided.")
else:
    print(f"Number of arguments: {len(sys.argv) - 1}")
