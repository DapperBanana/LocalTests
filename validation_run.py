
import math

def sector_area(radius, angle):
    if angle > 360:
        return "Angle must be less than or equal to 360 degrees"
    
    area = (math.pi * radius**2 * angle) / 360
    return area

radius = float(input("Enter the radius of the sector: "))
angle = float(input("Enter the angle of the sector in degrees: "))

result = sector_area(radius, angle)
print(f"The area of the sector with radius {radius} and angle {angle} degrees is: {result}")
