
import math

def area_of_hexagon(side_length):
    return ((3 * math.sqrt(3)) / 2) * (side_length ** 2)

side_length = float(input("Enter the side length of the regular hexagon: "))
area = area_of_hexagon(side_length)
print(f"The area of the regular hexagon is: {area}")
