'''The Head of Computing at the University of Poppleton is tasked with dividing a
group of students into lab groups. A lab group is usually 24 students, but this is
sometimes varied to create groups of similar size. Write a program that promptsfor
the number of students and group size, and then displays how many groups will be
needed and how many will be left over in a smaller group.
How many students? 113
Required group size? 22
There will be 5 groups with 3 students left over.
For bonus credit, see if you can fix the grammar in the output. So if there were 101
students in groups of 20 the output would be:
There will be 5 groups with 1 student left over.'''


students = int(input("How many students? "))
group_size = int(input("Required group size? "))
groups = students // group_size
left_over = students % group_size
group_word = "groups" if groups != 1 else "group"
student_word = "students" if left_over != 1 else "student"
print(f"There will be {groups} {group_word} with {left_over} {student_word} left over.")
