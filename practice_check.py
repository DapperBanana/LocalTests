
def area_of_trapezoidal_prism(base1, base2, height, prism_height):
    # Calculate the area of the trapezoid
    area_of_trapezoid = 0.5 * (base1 + base2) * height
    
    # Calculate the lateral area of the prism
    lateral_area = area_of_trapezoid * 2 + base1 * prism_height + base2 * prism_height
    
    # Calculate the total area of the trapezoidal prism
    total_area = lateral_area + 2 * base1 + 2 * base2
    
    return total_area

# Input values for the bases, height, and prism height
base1 = float(input("Enter the length of the first base: "))
base2 = float(input("Enter the length of the second base: "))
height = float(input("Enter the height of the trapezoid: "))
prism_height = float(input("Enter the height of the prism: "))

# Calculate and print the area of the trapezoidal prism
area = area_of_trapezoidal_prism(base1, base2, height, prism_height)
print(f"The area of the trapezoidal prism is: {area}")
