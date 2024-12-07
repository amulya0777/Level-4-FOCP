def encrypt_message(message):
    return ''.join(message.split())[::-1]

# Test
message = input("Enter a message to encrypt: ")
print(f"Encrypted message: {encrypt_message(message)}")
