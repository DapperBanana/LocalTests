
def calculate_pyramid_area(base_area, height):
    # Calculate the side area of the pyramid
    side_area = base_area + (1/2) * base_area
    
    # Calculate the total surface area of the pyramid
    total_area = base_area + side_area

    return total_area

base_area = float(input("Enter the base area of the pyramid: "))
height = float(input("Enter the height of the pyramid: "))

area = calculate_pyramid_area(base_area, height)
print(f"The total surface area of the pyramid is: {area}")
