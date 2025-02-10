
def calculate_pyramid_area(base_area, height):
    # Calculate the area of the pyramid using the formula: (1/3) * base_area * height
    area = (1/3) * base_area * height
    return area

# Input the base area and height of the pyramid
base_area = float(input("Enter the base area of the pyramid: "))
height = float(input("Enter the height of the pyramid: "))

# Calculate the area of the pyramid
pyramid_area = calculate_pyramid_area(base_area, height)

print(f"The area of the pyramid is: {pyramid_area}")
