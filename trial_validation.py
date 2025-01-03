
import cmath

def find_roots(a, b, c):
    discriminant = (b**2) - (4*a*c)
    sqrt_disc = cmath.sqrt(discriminant)

    root1 = (-b + sqrt_disc) / (2*a)
    root2 = (-b - sqrt_disc) / (2*a)

    return root1, root2

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

root1, root2 = find_roots(a, b, c)

print(f"The roots of the quadratic equation are: {root1} and {root2}")
