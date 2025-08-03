# Check if a word is a Palindrome

# Palindrome a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam or racecar.

print("\n --- Checking for Palindrome ---")

a = input("Enter a Word please: ")

a_list = list(a)
a_list.reverse()

A = ''.join(a_list)

if a == A:
    print("word is a palindrome!")

else:
    print("word is not a palindrome!")

print(f"{a} = {A}")