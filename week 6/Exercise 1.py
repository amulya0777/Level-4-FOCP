'''Write a function that accepts a positive integer as a parameter and then returns a
representation of that number in binary (base 2).
'''

def to_binary(n):
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

# Test
number = int(input("Enter a positive integer: "))
print(f"The binary representation of {number} is {to_binary(number)}.")
