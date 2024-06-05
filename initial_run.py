
import math

def area_of_pentagon(side_length):
    apothem = side_length / (2 * math.tan(math.pi/5))
    area = (5 * side_length * apothem) / 2
    return area

side_length = float(input("Enter the side length of the pentagon: "))
print("The area of the pentagon is:", area_of_pentagon(side_length))
