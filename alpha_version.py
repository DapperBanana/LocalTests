
# Function to swap two variables without using a temporary variable
def swap_variables(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

# Input variables
a = 10
b = 20

print("Before swapping:")
print("a =", a)
print("b =", b)

# Call function to swap variables
a, b = swap_variables(a, b)

print("After swapping:")
print("a =", a)
print("b =", b)
