
import cmath

# Function to find the roots of a quadratic equation
def find_roots(a, b, c):
    # Calculate the discriminant
    d = (b ** 2) - (4 * a * c)
    
    # Find the roots
    root1 = (-b + cmath.sqrt(d)) / (2 * a)
    root2 = (-b - cmath.sqrt(d)) / (2 * a)
    
    return root1, root2

# Input coefficients of the quadratic equation
a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))

# Find the roots and display the result
root1, root2 = find_roots(a, b, c)
print(f"The roots of the quadratic equation are: {root1} and {root2}")
