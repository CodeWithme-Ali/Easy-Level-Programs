# Program to sum all elements in a list.

print("\n--- Sum Elements in a List ---\n ")
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

total = sum(numbers)
print("Sum of all elements:", total)
