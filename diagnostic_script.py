
import math

def calculate_hexagon_area(side_length):
    area = (3 * math.sqrt(3) * side_length**2) / 2
    return area

side_length = float(input("Enter the side length of the regular hexagon: "))

area = calculate_hexagon_area(side_length)
print(f"The area of the regular hexagon is: {area}")
