
import math

def findRoots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root,
    else:
        return None

# example usage
a = 1
b = -3
c = 2
roots = findRoots(a, b, c)

if roots:
    if len(roots) == 2:
        print("The quadratic equation has two real roots:", roots[0], "and", roots[1])
    else:
        print("The quadratic equation has one real root:", roots[0])
else:
    print("The quadratic equation has no real roots")
