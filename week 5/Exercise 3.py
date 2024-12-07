import sys

if len(sys.argv) == 1:
    print("No arguments were provided.")
else:
    shortest = min(sys.argv[1:], key=len)
    print(f"The shortest argument is: {shortest}")
