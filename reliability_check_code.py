
def pyramid_area(base_area, height):
    # Calculating the lateral area of the pyramid
    lateral_area = base_area + (2 * base_area * height) / 2
    
    # Calculating the total area of the pyramid
    total_area = lateral_area + base_area
    
    return total_area

base_area = float(input("Enter the base area of the pyramid: "))
height = float(input("Enter the height of the pyramid: "))

area = pyramid_area(base_area, height)
print("The area of the pyramid is:", area)
