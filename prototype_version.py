
import math

def area_of_pentagonal_prism(side_length, height):
    # Calculate the area of one triangular face of the prism
    triangular_face_area = (math.sqrt(5 * (5 + 2 * math.sqrt(5))) * side_length ** 2) / 4

    # Calculate the area of the pentagonal base
    pentagon_area = (5 * triangular_face_area) / 2

    # Calculate the area of the two triangular faces
    triangular_face_area = (math.sqrt(5 * (5 + 2 * math.sqrt(5))) * side_length * height) / 2

    # Calculate the total surface area of the prism
    total_area = (2 * pentagon_area) + (5 * triangular_face_area)

    return total_area

# Test the function
side_length = 8
height = 12
area = area_of_pentagonal_prism(side_length, height)
print("The area of the pentagonal prism is", area)
