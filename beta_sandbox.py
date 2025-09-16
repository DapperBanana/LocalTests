
import math

def area_of_regular_polygon(n, s):
    area = (n * s**2) / (4 * math.tan(math.pi/n))
    return area

n = int(input("Enter the number of sides of the regular polygon: "))
s = float(input("Enter the length of each side of the regular polygon: "))

area = area_of_regular_polygon(n, s)
print(f"The area of the regular polygon is: {area}")
