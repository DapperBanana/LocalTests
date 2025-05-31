
# Swapping values of two variables without using a temporary variable

def swap_values(a, b):
    print(f"Before swapping: a={a}, b={b}")
    
    a = a + b
    b = a - b
    a = a - b
    
    print(f"After swapping: a={a}, b={b}")
    
# Test
a = 10
b = 20
swap_values(a, b)
