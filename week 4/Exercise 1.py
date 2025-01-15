'''Functions are oen used to validate input. Write a function that accepts a single
integer as a parameter and returns True if the integer is in the range 0 to 100
(inclusive), or False otherwise. Write a short program to test the function.'''


def testcase(x):
    if x >= 0 and x<=100:
        return True
    else:
        return False
num = int(input("Enter a number: "))
print(testcase(num))