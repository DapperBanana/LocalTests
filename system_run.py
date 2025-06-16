
def calculate_pyramid_area(base_area, height):
    # Calculate the slant height of the pyramid
    slant_height = (base_area ** 0.5) ** 2 + height ** 2

    # Calculate the surface area of the pyramid
    surface_area = base_area + 0.5 * (base_area ** 0.5) * slant_height

    return surface_area

base_area = float(input("Enter the base area of the pyramid: "))
height = float(input("Enter the height of the pyramid: "))

pyramid_area = calculate_pyramid_area(base_area, height)

print("The area of the pyramid is:", pyramid_area)
