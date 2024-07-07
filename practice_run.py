
# Function to swap values of two variables without using a temporary variable
def swap_values(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

# Input values for variables a and b
a = 5
b = 10

print("Before swapping:")
print("a =", a)
print("b =", b)

# Swap the values of a and b
a, b = swap_values(a, b)

print("After swapping:")
print("a =", a)
print("b =", b)
