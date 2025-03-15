
def calculate_pyramid_area(base_area, height):
    # Calculate the slant height of the pyramid
    slant_height = (base_area ** 2 + height ** 2) ** 0.5
    
    # Calculate the surface area of the pyramid
    base_perimeter = 4 * (base_area ** 0.5)
    lateral_area = base_perimeter * slant_height / 2
    total_area = base_area + lateral_area
    
    return total_area

base_area = float(input("Enter the base area of the pyramid: "))
height = float(input("Enter the height of the pyramid: "))

area = calculate_pyramid_area(base_area, height)
print(f"The total surface area of the pyramid is: {area}")
