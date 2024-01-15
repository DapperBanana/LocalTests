
import math

def find_roots(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Check if the discriminant is positive, zero, or negative
    if discriminant > 0:
        # Two distinct real roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        # One real root (the equation has a repeated root)
        root = -b / (2*a)
        return root,
    else:
        # Two complex roots
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        return complex(real_part, imaginary_part), complex(real_part, -imaginary_part)

# Test the function
a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))

roots = find_roots(a, b, c)

if len(roots) == 1:
    print("The equation has one real root:", roots[0])
elif len(roots) == 2:
    print("The equation has two distinct real roots:", roots[0], "and", roots[1])
else:
    print("The equation has two complex roots:", roots[0], "and", roots[1])
