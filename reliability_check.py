
import math

def pentagonal_prism_area(side_length, height):
    # Calculate the area of the pentagonal base
    base_area = 5/4 * side_length**2 * (1/math.tan(math.pi/5))
    
    # Calculate the lateral area of the prism
    lateral_area = 5 * side_length * height
    
    # Calculate the total area of the prism
    total_area = 2 * base_area + lateral_area
    
    return total_area

# Input the side length and height of the pentagonal prism
side_length = float(input("Enter the side length of the pentagon: "))
height = float(input("Enter the height of the prism: "))

# Calculate and print the area of the pentagonal prism
area = pentagonal_prism_area(side_length, height)
print("The area of the regular pentagonal prism is:", area)
