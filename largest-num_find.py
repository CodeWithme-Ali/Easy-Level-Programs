# Program to find the largest of three numbers.

print("\n --- Largest Number ---")
num1 = int(input("Enter a Number: "))
num2 = int(input("Enter a Number: "))
num3 = int(input("Enter a Number: "))

if num1 > num2 and num1 > num3:
    print(num1,"is greater!")

elif num2 > num1 and num2 > num3:
    print(num2,"is greater!")

elif num3 > num1 and num3 > num2:
    print(num3,"is greater!")

else:
    ("please enter number only!")    

