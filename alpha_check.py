
import math

def pentagonal_prism_area(side_length, height):
    perimeter = 5 * side_length
    apothem = side_length / (2 * math.tan(math.pi / 5))
    
    lateral_area = perimeter * height
    base_area = (5 * side_length * apothem) / 2
    total_area = 2 * base_area + lateral_area
    
    return total_area

side_length = float(input("Enter the side length of the pentagon: "))
height = float(input("Enter the height of the prism: "))

area = pentagonal_prism_area(side_length, height)
print(f"The area of the regular pentagonal prism is: {area:.2f}")
