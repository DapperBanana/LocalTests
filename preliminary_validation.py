
import math

def calculate_area(num_sides, side_length):
    """
    Calculates the area of a regular polygon given the number of sides and the length of each side.
    """
    area = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))
    return area

# Example usage
num_sides = int(input("Enter the number of sides of the polygon: "))
side_length = float(input("Enter the length of each side: "))

area = calculate_area(num_sides, side_length)
print("The area of the regular polygon is", area)
