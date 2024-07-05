
import math

def area_pentagonal_prism(side_length, height):
    # Calculate the area of one pentagon
    area_pentagon = (5 * side_length ** 2) / (4 * math.tan(math.pi / 5))
    
    # Calculate the area of the two pentagons
    area_base = 2 * area_pentagon
    
    # Calculate the area of the five rectangles
    perimeter = 5 * side_length
    area_side = perimeter * height
    
    # Calculate the total area of the pentagonal prism
    total_area = area_base + area_side
    
    return total_area

# Input side length and height of the pentagonal prism
side_length = float(input("Enter the side length of the pentagon: "))
height = float(input("Enter the height of the prism: "))

# Calculate and print the area of the pentagonal prism
print("The area of the regular pentagonal prism is:", area_pentagonal_prism(side_length, height))
