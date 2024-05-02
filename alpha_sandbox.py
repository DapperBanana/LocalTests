
import math

def pentagonal_prism_area(side_length, height):
    # Calculate the apothem (distance from the center of the pentagon to the midpoint of a side)
    apothem = side_length / (2 * math.tan(math.pi/5))
    
    # Calculate the area of one pentagonal face
    face_area = (5/2) * side_length * apothem
    
    # Calculate the lateral surface area
    lateral_area = 5 * side_length * height
    
    # Calculate the total surface area
    total_area = 2 * face_area + lateral_area
    
    return lateral_area, total_area

side_length = float(input("Enter the side length of the pentagon: "))
height = float(input("Enter the height of the prism: "))

lateral_area, total_area = pentagonal_prism_area(side_length, height)

print("The lateral area of the pentagonal prism is: ", lateral_area)
print("The total area of the pentagonal prism is: ", total_area)
