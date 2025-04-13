
# Function to swap the values of two variables without using a temporary variable
def swap_values(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

# Taking input from user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Swapping the values of a and b
a, b = swap_values(a, b)

print("After swapping:")
print("First number:", a)
print("Second number:", b)
