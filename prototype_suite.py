
import math

def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        
        return root1, root2

# Input coefficients of the quadratic equation
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

roots = find_roots(a, b, c)

if type(roots) == tuple:
    print("The roots are:", roots[0], "and", roots[1])
elif type(roots) == float:
    print("The root is:", roots)
else:
    print("The roots are complex numbers:", roots[0], "and", roots[1])
