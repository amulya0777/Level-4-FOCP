'''Last week you wrote a program that processed a collection of temperature readings
entered by the user and displayed the maximum, minimum, and mean. Create a
version of that program that takes the values from the command-line instead. Be
sure to handle the case where no arguments are provided!
'''

import sys

if len(sys.argv) < 2:
    print("No temperatures provided.")
else:
    try:
        temps = list(map(float, sys.argv[1:]))
        print(f"Max: {max(temps)}")
        print(f"Min: {min(temps)}")
        print(f"Mean: {sum(temps) / len(temps)}")
    except ValueError:
        print("Please provide valid numbers as temperature readings.")
