
def calculate_pyramid_area(base_area, height):
    base_area = float(base_area)
    height = float(height)
    
    pyramid_area = base_area + (base_area * 4 * (height**2))**0.5
    
    return pyramid_area

base_area = input("Enter the base area of the pyramid: ")
height = input("Enter the height of the pyramid: ")

area = calculate_pyramid_area(base_area, height)
print(f"The area of the pyramid is: {area}")
