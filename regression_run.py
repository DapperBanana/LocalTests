
import math

def calculate_distance(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return distance

point1 = (1, 2, 3)
point2 = (4, 5, 6)
distance = calculate_distance(point1, point2)

print(f"The distance between {point1} and {point2} is {distance}.")
