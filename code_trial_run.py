
import math

def sector_area(radius, angle):
    area = math.pi * radius**2 * (angle / 360)
    return area

radius = float(input("Enter the radius of the sector: "))
angle = float(input("Enter the angle of the sector in degrees: "))

area = sector_area(radius, angle)
print("The area of the sector is: ", round(area, 2))
