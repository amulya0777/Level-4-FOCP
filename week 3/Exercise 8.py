'''Modify the "Times Table" again so that the user still enters the number of the table,
but if this number is negative the table is printed backwards. So entering "-7"
would produce the Seven Times Table starting at "12 times" down to "0 times".'''

number = int(input("Enter the number for the times table (can be negative): "))
if number >= 0:
    for i in range(13):
        print(f"{i} x {number} = {i * number}")
else:
    for i in range(12, -1, -1):
        print(f"{i} x {-number} = {i * -number}")
