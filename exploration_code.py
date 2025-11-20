
import math

def calculate_distance(x1, y1, z1, x2, y2, z2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return distance

# Input coordinates of two points
x1, y1, z1 = 1, 2, 3
x2, y2, z2 = 4, 5, 6

# Calculate distance between the two points
distance = calculate_distance(x1, y1, z1, x2, y2, z2)

print(f"The distance between the two points is: {distance}")
