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
