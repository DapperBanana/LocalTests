
# Function to swap values of two variables without using a temporary variable
def swap_values(a, b):
    print("Before swapping:")
    print("a =", a)
    print("b =", b)
    
    a = a + b
    b = a - b
    a = a - b
    
    print("After swapping:")
    print("a =", a)
    print("b =", b)


# Main code
a = 10
b = 20

swap_values(a, b)
