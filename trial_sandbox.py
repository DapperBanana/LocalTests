
import cmath

def find_roots(a, b, c):
    # calculate the discriminant
    d = (b**2) - (4*a*c)
    
    # find the roots
    root1 = (-b + cmath.sqrt(d)) / (2*a)
    root2 = (-b - cmath.sqrt(d)) / (2*a)
    
    return root1, root2

# input parameters for the quadratic equation
a = 1
b = 5
c = 6

root1, root2 = find_roots(a, b, c)
print(f"The roots of the quadratic equation {a}x^2 + {b}x + {c} are: {root1} and {root2}")
