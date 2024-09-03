
import math

def calculate_icosahedron_area(side_length):
    area = 5 * math.sqrt(3) * (side_length ** 2)
    return area

side_length = float(input("Enter the side length of the icosahedron: "))
area = calculate_icosahedron_area(side_length)

print("The area of the regular icosahedron with side length", side_length, "is", area)
