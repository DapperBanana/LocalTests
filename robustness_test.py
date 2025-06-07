
def trapezoidal_prism_area(a, b, h1, h2, height):
    # Calculate the area of the trapezoid
    trapezoid_area = 0.5 * (a + b) * height
    
    # Calculate the lateral surface area of the prism
    lateral_area = (a + b) * height
    
    # Calculate the total surface area of the trapezoidal prism
    total_area = 2 * trapezoid_area + lateral_area
    
    return total_area

# Input the dimensions of the trapezoidal prism
a = float(input("Enter the length of the top base of the trapezoid: "))
b = float(input("Enter the length of the bottom base of the trapezoid: "))
h1 = float(input("Enter the height of the trapezoid: "))
h2 = float(input("Enter the height of the prism: "))
height = float(input("Enter the height of the prism: "))

# Calculate the total area of the trapezoidal prism
area = trapezoidal_prism_area(a, b, h1, h2, height)

print(f"The total surface area of the trapezoidal prism is: {area}")
