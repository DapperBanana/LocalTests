
import math

def area_of_pentagon(side_length):
    apothem_length = side_length / (2 * math.tan(math.pi/5))
    area = (5/2) * side_length * apothem_length
    return area

side_length = float(input("Enter the side length of the pentagon: "))
area = area_of_pentagon(side_length)
print(f"The area of the pentagon is: {area}")
