
def calculate_pyramid_area(base_area, height):
    # Calculate the area of the pyramid using the formula: (base_area + base_area * height / 2)
    pyramid_area = base_area + base_area * height / 2
    return pyramid_area

# Input base area and height from the user
base_area = float(input("Enter the base area of the pyramid: "))
height = float(input("Enter the height of the pyramid: "))

# Calculate the area of the pyramid
area = calculate_pyramid_area(base_area, height)

# Output the area of the pyramid
print(f"The area of the pyramid is: {area}")
