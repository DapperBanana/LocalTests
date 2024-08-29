
import math

def area_pentagonal_prism(side_length: float, height: float) -> float:
    perimeter = 5 * side_length
    apothem = side_length / (2 * math.tan(math.pi / 5))
    base_area = (5 * side_length * apothem) / 2
    side_area = perimeter * height
    total_area = 2 * base_area + side_area
    return total_area

side_length = float(input("Enter the side length of the pentagon: "))
height = float(input("Enter the height of the prism: "))

area = area_pentagonal_prism(side_length, height)
print(f"The area of the regular pentagonal prism is: {area}")
