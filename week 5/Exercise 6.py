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
