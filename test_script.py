
def calculate_pyramid_area(base_area, height):
    # Calculate the area of the pyramid: (base area + 0.5 * base perimeter * height)
    base_perimeter = (base_area ** 0.5) * 4
    pyramid_area = base_area + 0.5 * base_perimeter * height
    return pyramid_area

# Input base area and height from the user
base_area = float(input("Enter the base area of the pyramid: "))
height = float(input("Enter the height of the pyramid: "))

# Calculate the area of the pyramid
area = calculate_pyramid_area(base_area, height)

print(f"The area of the pyramid is: {area}")
