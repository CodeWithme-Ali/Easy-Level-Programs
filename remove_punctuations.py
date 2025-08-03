# Remove all punctuations from a string.

print("\n --- Program Removes Punctuations ---")

a = input("Enter String: ")

punctuations = '''!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~'''

for i in punctuations:
    a = a.replace(i,'')

print(a)
