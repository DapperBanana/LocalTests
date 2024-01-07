
import math

def area_of_regular_polygon(side_length, num_sides):
    """
    Calculate the area of a regular polygon.
    :param side_length: the length of each side of the polygon
    :param num_sides: the number of sides of the polygon
    :return: the area of the polygon
    """
    apothem = side_length / (2 * math.tan(math.pi / num_sides))
    area = (num_sides * side_length * apothem) / 2
    return area

# Example usage
side_length = 5
num_sides = 6
area = area_of_regular_polygon(side_length, num_sides)
print(f"The area of the regular polygon is: {area}")
