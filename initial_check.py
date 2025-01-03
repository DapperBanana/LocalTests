
def calculate_pyramid_area(base_area, height):
    # Calculate the area of the pyramid using the formula: (base_area + (0.5 * base_perimeter * slant_height))
    base_perimeter = 4 * ((base_area ** 0.5) / 2)  # Formula for perimeter of square base
    slant_height = ((height ** 2) + ((base_area ** 0.5) / 2) ** 2) ** 0.5  # Formula for slant height

    pyramid_area = base_area + (0.5 * base_perimeter * slant_height)
    return pyramid_area

# Input base area and height of the pyramid
base_area = float(input("Enter the base area of the pyramid: "))
height = float(input("Enter the height of the pyramid: "))

# Calculate the area of the pyramid
area = calculate_pyramid_area(base_area, height)

print("The area of the pyramid is:", area)
