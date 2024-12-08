from collections import Counter

def frequency_analysis(text):
    counts = Counter(char for char in text.lower() if char.isalpha())
    return counts.most_common(6)

# Test
text = input("Enter the text to analyze: ")
analysis = frequency_analysis(text)
print("Most common letters and their counts:")
for letter, count in analysis:
    print(f"{letter}: {count}")
