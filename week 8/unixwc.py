import sys

if len(sys.argv) != 2:
    print("Usage: python wc.py <filename>")
else:
    filename = sys.argv[1]
    
    try:
        with open(filename, 'r') as file:
            lines = 0
            characters = 0
            for line in file:
                lines += 1
                characters += len(line)
                
            print(f"Lines: {lines}")
            print(f"Characters: {characters}")
    except:
        print(f"Error: The file '{filename}' could not be opened.")
