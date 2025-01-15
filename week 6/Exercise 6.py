'''Write a program that decrypts messages encoded as above.
'''

def decrypt_message(encrypted, interval):
    return ''.join([encrypted[i] for i in range(0, len(encrypted), interval)])

# Test
encrypted_message = input("Enter the encrypted message: ")
interval = int(input("Enter the interval used for encryption: "))
print(f"Decrypted message: {decrypt_message(encrypted_message, interval)}")
