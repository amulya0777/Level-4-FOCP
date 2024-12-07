def unique_letters(s):
    return sorted(set(s))

# Test
string = input("Enter a string: ")
print(f"Unique letters: {unique_letters(string)}")
