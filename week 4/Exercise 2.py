'''Write a function that has a single string as its parameter, and returns the number of
uppercase letters, and the number of lowercase letters in the string. Test the
function with a short program.'''


def teststring(name):
    upper = 0
    lower = 0
    for x in name:
        if ord(x) >= 65 and ord(x)<= 90:
            upper = upper + 1
        elif ord(x) >= 97 and ord(x) <= 122:
            lower = lower + 1
        else:
            continue
    print(f'There are {upper} uppercase letters and {lower} lowercase letters. ')
message = input("Enter a string: ")
teststring(message)
