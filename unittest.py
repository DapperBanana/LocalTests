
import math

def distance_3d(x1, y1, z1, x2, y2, z2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return distance

# Input points coordinates
x1 = float(input("Enter x-coordinate of point 1: "))
y1 = float(input("Enter y-coordinate of point 1: "))
z1 = float(input("Enter z-coordinate of point 1: "))
x2 = float(input("Enter x-coordinate of point 2: "))
y2 = float(input("Enter y-coordinate of point 2: "))
z2 = float(input("Enter z-coordinate of point 2: "))

# Calculate distance
result = distance_3d(x1, y1, z1, x2, y2, z2)
print(f"The distance between the two points is: {result}")
