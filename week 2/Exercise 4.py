'''A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
first count the sweets and then divide them according to how many pupils attend
that day. Write a program that will tell the teacher how many sweets to give to each
pupil, and how many she will have left over.
'''


sweets = int(input("How many sweets? "))
pupils = int(input("How many pupils? "))
sweets_per_pupil = sweets // pupils
left_over = sweets % pupils
print(f"Each pupil gets {sweets_per_pupil} sweets, with {left_over} left over.")
