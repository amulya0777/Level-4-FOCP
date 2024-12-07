students = int(input("How many students? "))
group_size = int(input("Required group size? "))
groups = students // group_size
left_over = students % group_size
group_word = "groups" if groups != 1 else "group"
student_word = "students" if left_over != 1 else "student"
print(f"There will be {groups} {group_word} with {left_over} {student_word} left over.")
