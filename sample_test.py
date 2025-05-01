
def area_of_trapezoidal_prism(base1, base2, height, length):
    # Area of trapezoid
    area_of_trapezoid = 0.5 * (base1 + base2) * height
    
    # Area of trapezoidal prism
    area_of_prism = 2 * area_of_trapezoid + (base1 + base2) * length
    
    return area_of_prism

# Input values
base1 = float(input("Enter the length of base 1 of the trapezoid: "))
base2 = float(input("Enter the length of base 2 of the trapezoid: "))
height = float(input("Enter the height of the trapezoid: "))
length = float(input("Enter the length of the prism: "))

# Calculate and print the area of the trapezoidal prism
print("The area of the trapezoidal prism is:", area_of_trapezoidal_prism(base1, base2, height, length))
