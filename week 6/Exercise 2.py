def factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

# Test
number = int(input("Enter a positive integer: "))
print(f"The factors of {number} are: {factors(number)}.")
