
import math

def calculate_area_of_polygon(n, s):
    area = (n * s**2) / (4 * math.tan(math.pi/n))
    return area

n = int(input("Enter the number of sides: "))
s = float(input("Enter the length of each side: "))

area = calculate_area_of_polygon(n, s)
print("The area of the regular polygon is:", area)
