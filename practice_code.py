
import math

def calculate_hexagon_area(side):
    area = (3 * math.sqrt(3) * side**2) / 2
    return area

# Example usage
side_length = float(input("Enter the side length of the hexagon: "))
hexagon_area = calculate_hexagon_area(side_length)
print("Area of the hexagon:", hexagon_area)
