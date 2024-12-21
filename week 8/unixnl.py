import sys

if len(sys.argv) != 2:
    print("Usage: python nl.py <filename>")
else:
    try:
        with open(sys.argv[1], 'r') as file:
            for line_number, line in enumerate(file, start=1):
                print(f"{line_number}\t{line}", end='')
    except:
        print(f"Error: The file '{sys.argv[1]}' does not exist.")
