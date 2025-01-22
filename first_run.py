
# Function to swap the values of two variables without using a temporary variable
def swap_values(x, y):
    x = x + y
    y = x - y
    x = x - y
    return x, y

# Input values from the user
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

# Swapping values without using a temporary variable
x, y = swap_values(x, y)

# Output the swapped values
print("After swapping:")
print("First number:", x)
print("Second number:", y)
