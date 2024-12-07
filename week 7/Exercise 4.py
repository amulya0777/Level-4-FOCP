from collections import Counter

def frequency_analysis(text):
    counts = Counter(text.lower())
    letters_only = {char: count for char, count in counts.items() if char.isalpha()}
    most_common = sorted(letters_only.items(), key=lambda x: (-x[1], x[0]))[:6]
    return most_common

# Test
text = input("Enter the text to analyze: ")
analysis = frequency_analysis(text)
print("Most common letters and their counts:")
for letter, count in analysis:
    print(f"{letter}: {count}")
