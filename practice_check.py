
import math

def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print("The roots are:", root1, "and", root2)
    elif discriminant == 0:
        root = -b / (2*a)
        print("The only root is:", root)
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        print("The roots are complex:", str(real_part) + " + " + str(imaginary_part) + "i", "and", str(real_part) + " - " + str(imaginary_part) + "i")
        
if __name__ == "__main__":
    a = float(input("Enter the coefficient of x^2: "))
    b = float(input("Enter the coefficient of x: "))
    c = float(input("Enter the constant term: "))
    
    find_roots(a, b, c)
