def testcase(x):
    if x >= 0 and x<=100:
        return True
    else:
        return False
num = int(input("Enter a number: "))
print(testcase(num))