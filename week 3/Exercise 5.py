BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    password1 = input("Enter a new password: ")
    password2 = input("Re-enter the password: ")
    if password1 == password2 and 8 <= len(password1) <= 12 and password1 not in BAD_PASSWORDS:
        print("Password Set")
        break
    else:
        print("Error: Password is invalid. Try again.")
