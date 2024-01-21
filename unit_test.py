
def calculate_pyramid_area(base_area, height):
    # Calculate the slant height of the pyramid using Pythagorean theorem
    slant_height = (base_area ** 0.5 + height ** 2) ** 0.5

    # Calculate the lateral area of the pyramid
    lateral_area = base_area + (base_area * slant_height) / 2

    # Calculate the total area of the pyramid
    total_area = base_area + lateral_area

    # Return the total area of the pyramid
    return total_area


# Test the function with sample inputs
base_area = 16
height = 8

pyramid_area = calculate_pyramid_area(base_area, height)
print("The area of the pyramid is:", pyramid_area)
