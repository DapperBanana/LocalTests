
import math

def distance_3d(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

x1, y1, z1 = 1, 2, 3
x2, y2, z2 = 4, 5, 6

distance = distance_3d(x1, y1, z1, x2, y2, z2)
print(f"The distance between points ({x1}, {y1}, {z1}) and ({x2}, {y2}, {z2}) is {distance}")
