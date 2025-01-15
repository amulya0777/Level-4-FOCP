'''Write a program that takes the name of a file as a command-line argument, and
creates a backup copy of that file. The backup should contain an exact copy of the
contents of the original and should, obviously, have a dierent name.
'''

import sys
import shutil

if len(sys.argv) != 2:
    print("Usage: python script.py <filename>")
else:
    source_file = sys.argv[1]
    backup_file = source_file + ".backup"
    try:
        shutil.copy(source_file, backup_file)
        print(f"Backup created: {backup_file}")
    except FileNotFoundError:
        print(f"File not found: {source_file}")
    except Exception as e:
        print(f"Error creating backup: {e}")
