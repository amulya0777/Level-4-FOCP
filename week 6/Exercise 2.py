'''Write and test a function that takes an integer as its parameter and returns the
factors of that integer. (A factor is an integer which can be multiplied by another to
yield the original).
'''

def factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

# Test
number = int(input("Enter a positive integer: "))
print(f"The factors of {number} are: {factors(number)}.")
