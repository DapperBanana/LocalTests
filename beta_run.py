
import math

def area_of_decagon(side_length):
    # Calculate the apothem of the decagon
    apothem = side_length / (2 * math.tan(math.pi / 10))
    
    # Calculate the area of the decagon
    area = (5 * side_length * apothem) / 2
    
    return area

# Example usage
side_length = float(input("Enter the length of the side of the decagon: "))
area = area_of_decagon(side_length)
print("The area of the regular decagon is:", area)
