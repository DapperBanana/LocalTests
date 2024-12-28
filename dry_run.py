
import cmath

def find_roots(a, b, c):
    d = (b**2) - (4*a*c)
    
    # find two solutions
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    
    return sol1, sol2

# input coefficients of the quadratic equation
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

root1, root2 = find_roots(a, b, c)
print("The roots are: {0} and {1}".format(root1, root2))
