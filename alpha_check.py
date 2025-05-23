
import cmath

def find_roots(a, b, c):
    # calculate the discriminant
    discriminant = (b**2) - (4*a*c)
    
    # find two roots
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    
    return root1, root2

# take input of coefficients from user
a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))

# find the roots
root1, root2 = find_roots(a, b, c)

print(f"The roots of the quadratic equation are: {root1} and {root2}")
