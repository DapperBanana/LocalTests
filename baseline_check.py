
import cmath

def find_roots(a, b, c):
    discriminant = (b**2) - (4*a*c)
    
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    
    return root1, root2

a = float(input("Enter the value of coefficient a: "))
b = float(input("Enter the value of coefficient b: "))
c = float(input("Enter the value of coefficient c: "))

root1, root2 = find_roots(a, b, c)

print("The roots of the quadratic equation are: {} and {}.".format(root1, root2))
