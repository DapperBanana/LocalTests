
import math

def pentagonal_prism_area(side_length, height):
    apothem = side_length / (2 * math.tan(math.radians(180 / 5)))
    base_area = 5 * side_length * apothem / 2
    side_area = 5 * side_length * height
    total_area = base_area + side_area
    return total_area

side_length = float(input("Enter the side length of the pentagon: "))
height = float(input("Enter the height of the prism: "))

area = pentagonal_prism_area(side_length, height)

print(f"The area of the regular pentagonal prism is: {area}")
