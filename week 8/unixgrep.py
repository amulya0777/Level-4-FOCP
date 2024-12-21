import sys

if len(sys.argv) != 3:
    print("Usage: python grep.py <pattern> <filename>")
else:
    pattern = sys.argv[1]
    filename = sys.argv[2]
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                if pattern in line:
                    print(line, end='')
    except:
        print(f"Error: The file '{filename}' could not be opened.")
