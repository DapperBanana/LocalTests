
import cmath

def find_roots(a, b, c):
    d = (b**2) - (4*a*c)
    root1 = (-b - cmath.sqrt(d)) / (2 * a)
    root2 = (-b + cmath.sqrt(d)) / (2 * a)
    return root1, root2

a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))

root1, root2 = find_roots(a, b, c)

print("The roots of the quadratic equation are: {0} and {1}".format(root1, root2))
