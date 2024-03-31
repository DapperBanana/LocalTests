
import math

def pentagonal_prism_area(base_side_length, prism_height):
    perimeter = 5 * base_side_length
    apothem = base_side_length / (2 * math.tan(math.pi / 5))
    
    base_area = 0.5 * perimeter * apothem
    side_area = perimeter * prism_height
    total_area = 2 * base_area + side_area
    
    return total_area

base_side_length = float(input("Enter the side length of the base of the pentagonal prism: "))
prism_height = float(input("Enter the height of the pentagonal prism: "))

area = pentagonal_prism_area(base_side_length, prism_height)
print("The area of the regular pentagonal prism is:", area)
