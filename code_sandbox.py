
import math

def calculate_area(side_length):
    area = 5 * math.sqrt(3) * side_length**2
    return area

side_length = float(input("Enter the side length of the icosahedron: "))
area = calculate_area(side_length)
print("The surface area of the icosahedron is:", area)
