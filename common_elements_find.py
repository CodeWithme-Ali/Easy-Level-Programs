# Program to find common elements in two lists.


print("\n --- Common Elements ---")
list1 = list(map(int, input("Enter first list (space-separated): ").split()))
list2 = list(map(int, input("Enter second list (space-separated): ").split()))

common = []
for item in list1:
    if item in list2 and item not in common:  # Avoid duplicates
        common.append(item)

print("Common elements:", common)
