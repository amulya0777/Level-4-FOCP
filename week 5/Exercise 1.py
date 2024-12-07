import sys
import platform

if len(sys.argv) > 1:
    print("This program does not take arguments.")
else:
    print(f"Operating system: {platform.system()}")
    print(f"Version: {platform.version()}")
