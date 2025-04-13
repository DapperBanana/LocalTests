
def calculate_pyramid_area(base_area, height):
    # Calculate the area of the pyramid using the formula: base_area + (base_perimeter * height) / 2
    base_perimeter = 2 * ((base_area) ** 0.5)
    pyramid_area = base_area + (base_perimeter * height) / 2
    return pyramid_area

# Input the base area and height of the pyramid
base_area = float(input("Enter the base area of the pyramid: "))
height = float(input("Enter the height of the pyramid: "))

# Calculate the area of the pyramid
result = calculate_pyramid_area(base_area, height)

# Display the result
print("The area of the pyramid is:", result)
