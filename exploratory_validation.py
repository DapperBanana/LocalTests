
import math

def calculate_icosahedron_area(edge_length):
    area = 5 * math.sqrt(3) * edge_length**2
    return area

# Test the function with an edge length of 5 units
edge_length = 5
area = calculate_icosahedron_area(edge_length)
print(f"The area of the regular icosahedron with edge length {edge_length} is: {area}")
