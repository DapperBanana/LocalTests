
import math

def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root, root
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2

# Input coefficients
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# Find and print roots
roots = find_roots(a, b, c)
print("Roots are:", roots)
