
import math

def calculate_distance(x1, y1, z1, x2, y2, z2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return distance

x1 = int(input("Enter the x-coordinate of point 1: "))
y1 = int(input("Enter the y-coordinate of point 1: "))
z1 = int(input("Enter the z-coordinate of point 1: "))
x2 = int(input("Enter the x-coordinate of point 2: "))
y2 = int(input("Enter the y-coordinate of point 2: "))
z2 = int(input("Enter the z-coordinate of point 2: "))

distance = calculate_distance(x1, y1, z1, x2, y2, z2)
print(f"The distance between the two points is: {distance}")
