import sys

if len(sys.argv) != 3:
    print("Usage: python diff.py <file1> <file2>")
else:
    try:
        with open(sys.argv[1], 'r') as file1, open(sys.argv[2], 'r') as file2:
            if file1.read() == file2.read():
                print("The files are the same.")
            else:
                print("The files are different.")
    except:
        print("Error: One or both files could not be opened.")
