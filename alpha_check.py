
import math

def calculate_hexagon_area(side_length):
    area = (3 * math.sqrt(3) * side_length ** 2) / 2
    return area

# Example usage
side_length = 5
hexagon_area = calculate_hexagon_area(side_length)
print("Area of the regular hexagon:", hexagon_area)
