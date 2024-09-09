
def calculate_pyramid_area(base_area, height):
    # Calculate the area of the pyramid: A = (base area + 0.5 * base area * height)
    pyramid_area = base_area + 0.5 * base_area * height
    return pyramid_area

base_area = float(input("Enter the base area of the pyramid: "))
height = float(input("Enter the height of the pyramid: "))

area = calculate_pyramid_area(base_area, height)

print(f"The area of the pyramid is: {area}")
