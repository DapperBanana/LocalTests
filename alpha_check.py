
import math

def calculate_area(side_length):
    area = (3 * math.sqrt(3) * side_length ** 2) / 2
    return area

# Example usage
side = float(input("Enter the side length of the hexagon: "))
hexagon_area = calculate_area(side)
print("The area of the regular hexagon is:", hexagon_area)
