name = input('Enter a name: ')

name1 = list(name)
n = len(name)
if n > 1:
    name1.pop(n-1)
    name2 = ''.join(name1)
    print(f'{name2}')
else:
    print(name)


