
# Program to swap values of two variables without using a temporary variable

# Input values for variables
a = int(input("Enter value for variable a: "))
b = int(input("Enter value for variable b: "))

# Swapping the values
a = a + b
b = a - b
a = a - b

# Output the swapped values
print("After swapping:")
print("Value of variable a:", a)
print("Value of variable b:", b)
