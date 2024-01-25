
import math

def calculate_frustum_area(r1, r2, h):
    area = math.pi * (r1 + r2) * math.sqrt((r2 - r1)**2 + h**2) + math.pi * (r1**2 + r2**2)
    return area

# Example usage
r1 = 5
r2 = 10
h = 8

frustum_area = calculate_frustum_area(r1, r2, h)
print("The area of the frustum of a cone is:", frustum_area)
