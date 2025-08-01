
import math

def calculate_distance(point1, point2):
    distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 + (point2[2] - point1[2])**2)
    return distance

point1 = (1, 2, 3)
point2 = (4, 5, 6)

distance = calculate_distance(point1, point2)
print(f"The distance between {point1} and {point2} is: {distance}")
