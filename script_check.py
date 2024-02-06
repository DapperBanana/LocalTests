
import math

def calculate_area_of_hexadecagon(side_length):
    # Calculate the apothem (the distance from the center to any side)
    apothem = side_length / (2 * math.tan(math.pi / 16))
    
    # Calculate the area of each triangle
    area_of_triangle = (side_length * apothem) / 2
    
    # Calculate the total area (the area of one triangle multiplied by 16)
    area_of_hexadecagon = area_of_triangle * 16
    
    return area_of_hexadecagon


# Example usage
side_length = 5
hexadecagon_area = calculate_area_of_hexadecagon(side_length)
print("The area of the regular hexadecagon is:", hexadecagon_area)
