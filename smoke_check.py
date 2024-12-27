
import math

def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print("The roots are:", root1, "and", root2)
    elif discriminant == 0:
        root = -b / (2*a)
        print("The root is:", root)
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        print("The roots are complex and are:", real_part, "+", imaginary_part, "i and ", real_part, "-", imaginary_part, "i")

# Example quadratic equation: 2x^2 + 5x + 2 = 0
a = 2
b = 5
c = 2

find_roots(a, b, c)
