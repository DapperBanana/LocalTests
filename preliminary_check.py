
import math

def pentagonal_prism_area(side_length, height):
    # Calculate the area of the pentagonal base
    base_area = (5 * side_length ** 2) / (4 * math.tan(math.pi/5))
    
    # Calculate the lateral surface area
    lateral_area = 5 * side_length * height
    
    # Calculate the total surface area
    total_area = 2 * base_area + lateral_area
    
    return total_area

# Taking input values from the user
side_length = float(input("Enter the side length of the pentagon: "))
height = float(input("Enter the height of the prism: "))

# Calculate and print the area of the prism
area = pentagonal_prism_area(side_length, height)
print(f"The area of the regular pentagonal prism is: {area}")
