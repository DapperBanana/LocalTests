
def trapezoidal_prism_area(a, b, h, H):
    # Calculate the area of the trapezoid base
    base_area = 0.5 * (a + b) * h
    
    # Calculate the lateral surface area of the prism
    lateral_area = 2 * ((a + b) * H)
    
    # Calculate the total surface area of the prism
    total_area = base_area + lateral_area
    
    return total_area

# Input values for the trapezoidal prism
a = float(input("Enter the length of the top side of the trapezoid (a): "))
b = float(input("Enter the length of the bottom side of the trapezoid (b): "))
h = float(input("Enter the height of the trapezoid (h): "))
H = float(input("Enter the height of the prism (H): "))

# Calculate the area of the trapezoidal prism
area = trapezoidal_prism_area(a, b, h, H)
print("The area of the trapezoidal prism is:", area)
