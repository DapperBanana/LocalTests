
def trapezoidal_prism_area(b1, b2, h, l):
    # Calculate the area of the trapezoid base
    base_area = 0.5 * (b1 + b2) * h
    
    # Calculate the lateral area of the prism
    lateral_area = (b1 + b2) * l
    
    # Calculate the total area of the trapezoidal prism
    total_area = 2 * base_area + lateral_area
    
    return total_area

# Input the dimensions of the trapezoidal prism
b1 = float(input("Enter the length of the top base of the trapezoid: "))
b2 = float(input("Enter the length of the bottom base of the trapezoid: "))
h = float(input("Enter the height of the trapezoid: "))
l = float(input("Enter the length of the prism: "))

# Calculate the area of the trapezoidal prism
area = trapezoidal_prism_area(b1, b2, h, l)

print(f"The area of the trapezoidal prism is: {area}")
