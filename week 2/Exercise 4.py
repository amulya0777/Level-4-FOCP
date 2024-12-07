sweets = int(input("How many sweets? "))
pupils = int(input("How many pupils? "))
sweets_per_pupil = sweets // pupils
left_over = sweets % pupils
print(f"Each pupil gets {sweets_per_pupil} sweets, with {left_over} left over.")
