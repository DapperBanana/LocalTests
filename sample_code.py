
def calculate_pyramid_area(base_area, height):
    return (base_area + (1/2) * (base_area * height))

base_area = float(input("Enter the base area of the pyramid: "))
height = float(input("Enter the height of the pyramid: "))

pyramid_area = calculate_pyramid_area(base_area, height)
print(f"The area of the pyramid is: {pyramid_area}")
