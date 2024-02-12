
import cmath

def find_roots(a, b, c):
    # Calculate the discriminant
    d = (b ** 2) - (4 * a * c)
    
    # find two solutions
    root1 = (-b - cmath.sqrt(d)) / (2 * a)
    root2 = (-b + cmath.sqrt(d)) / (2 * a)
    
    return root1, root2

# get user input
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# call the function and print the roots
root1, root2 = find_roots(a, b, c)
print("Roots are:", root1, root2)
