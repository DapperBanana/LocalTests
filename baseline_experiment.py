
def calculate_pyramid_area(base_area, height):
    # Calculate the area of the pyramid
    area = (base_area + base_area + ((base_area ** 2 + (4 * base_area * height)) ** 0.5)) / 2
    
    return area

# Input base area and height of the pyramid
base_area = float(input("Enter the base area of the pyramid: "))
height = float(input("Enter the height of the pyramid: "))

# Calculate the area of the pyramid
pyramid_area = calculate_pyramid_area(base_area, height)

print(f"The area of the pyramid is: {pyramid_area}")
