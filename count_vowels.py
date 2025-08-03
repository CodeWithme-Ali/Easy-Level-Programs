# Count vowels in a string.

print("\n--- Vowel Count ---\n ")

text = input("Enter a String: ")

vowel_count = 0 

for char in text:
    if char in "aeiouAEIOU":
        vowel_count += 1

print("\nNumber of vowels in a string:", vowel_count)
