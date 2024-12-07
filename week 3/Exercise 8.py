number = int(input("Enter the number for the times table (can be negative): "))
if number >= 0:
    for i in range(13):
        print(f"{i} x {number} = {i * number}")
else:
    for i in range(12, -1, -1):
        print(f"{i} x {-number} = {i * -number}")
