'''Modify your "greetings" program so that the first letter of the name entered is
always in uppercase with the rest in lowercase. This should happen even if the user
entered their name differently. So if the user entered arthur, ARTHUR, or even
arTHur the name should be displayed as Arthur.'''

name = input("Enter your name: ")
def capitalize(text):
    if text:
        result = text[0].upper() + text[1:].lower()
        print(f'Greetings Mr. {result}!')
    else:
        print("No name entered.")
capitalize(name)
