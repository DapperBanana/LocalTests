
import math

def area_of_pentagonal_prism(s, h):
    a = s / (2 * math.tan(math.pi / 5))  # Apothem length of the pentagon
    base_area = 5 * (0.5 * s * a)  # Area of the pentagon base
    lateral_area = 5 * s * h  # Area of the lateral faces
    total_area = base_area + lateral_area
    return total_area

# Input values
side_length = float(input("Enter the side length of the pentagon: "))
height = float(input("Enter the height of the prism: "))

# Calculate the area of the pentagonal prism
area = area_of_pentagonal_prism(side_length, height)

print(f"The area of the regular pentagonal prism is: {area:.2f}")
