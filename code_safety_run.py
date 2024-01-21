
import math

def calculate_distance(x1, y1, z1, x2, y2, z2):
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return distance

# Taking input from the user for the two points
x1 = float(input("Enter x-coordinate of the first point: "))
y1 = float(input("Enter y-coordinate of the first point: "))
z1 = float(input("Enter z-coordinate of the first point: "))

x2 = float(input("Enter x-coordinate of the second point: "))
y2 = float(input("Enter y-coordinate of the second point: "))
z2 = float(input("Enter z-coordinate of the second point: "))

# Calculating the distance between the two points
distance = calculate_distance(x1, y1, z1, x2, y2, z2)

# Printing the calculated distance
print("The distance between the two points is", distance)
