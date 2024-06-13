
# Function to swap values of two variables without using a temporary variable
def swap_values(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

# Input values for variables
var1 = 5
var2 = 10

# Display the original values
print("Original values:")
print("var1 =", var1)
print("var2 =", var2)

# Swap the values
var1, var2 = swap_values(var1, var2)

# Display the swapped values
print("\nSwapped values:")
print("var1 =", var1)
print("var2 =", var2)
