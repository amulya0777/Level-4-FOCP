'''Computers are commonly used in encryption. A very simple form of encryption
(more accurately "obfuscation") would be to remove the spaces from a message
and reverse the resulting string. Write, and test, a function that takes a string
containing a message and "encrypts" it in this way.
'''


def encrypt_message(message):
    return ''.join(message.split())[::-1]

# Test
message = input("Enter a message to encrypt: ")
print(f"Encrypted message: {encrypt_message(message)}")
