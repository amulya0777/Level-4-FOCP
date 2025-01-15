'''When processing data it is often useful to remove the last character from some
input (it is often a newline). Write and test a function that takes a string parameter
and returns it with the last character removed. (If the string contains one or fewer
characters, return it unchanged.)'''

name = input('Enter a name: ')

name1 = list(name)
n = len(name)
if n > 1:
    name1.pop(n-1)
    name2 = ''.join(name1)
    print(f'{name2}')
else:
    print(name)


