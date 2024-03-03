
# Function to swap values of two variables without using a temporary variable
def swap_values(a, b):
    print("Before swapping:")
    print("a =", a)
    print("b =", b)
    
    a = a + b
    b = a - b
    a = a - b
    
    print("\nAfter swapping:")
    print("a =", a)
    print("b =", b)

# Input values from user
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

# Call the function to swap values
swap_values(a, b)
