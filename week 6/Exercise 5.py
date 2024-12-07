import random

def random_encrypt(message):
    interval = random.randint(2, 20)
    encrypted = []
    for char in message:
        encrypted.append(char)
        encrypted.extend(random.choices('abcdefghijklmnopqrstuvwxyz', k=interval - 1))
    return ''.join(encrypted), interval

# Test
message = input("Enter a message to encrypt: ")
encrypted_message, interval_used = random_encrypt(message)
print(f"Encrypted message: {encrypted_message}")
print(f"Interval used: {interval_used}")
