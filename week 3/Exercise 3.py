'''Modify your previous program so that the password must be between 8 and 12
characters (inclusive) long.'''

password1 = input("Enter a new password: ")
password2 = input("Re-enter the password: ")
if password1 == password2 and 8 <= len(password1) <= 12:
    print("Password Set")
else:
    print("Error: Passwords do not match or are not between 8 and 12 characters")
