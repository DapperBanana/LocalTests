
import math

def frustum_area(radius1, radius2, height):
    base1_area = math.pi * radius1**2
    base2_area = math.pi * radius2**2
    side_area = math.pi * (radius1 + radius2) * math.sqrt((radius1 - radius2)**2 + height**2)
    
    area = base1_area + base2_area + side_area
    return area

radius1 = float(input("Enter the radius of the larger base of the frustum: "))
radius2 = float(input("Enter the radius of the smaller base of the frustum: "))
height = float(input("Enter the height of the frustum: "))

frustum_area = frustum_area(radius1, radius2, height)
print("The area of the frustum of a cone is: ", frustum_area)
