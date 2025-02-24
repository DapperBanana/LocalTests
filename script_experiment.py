
def calculate_pyramid_area(base_area, height):
    return (base_area + base_area**(1/2 + 2) * height) / 2

base_area = float(input("Enter the base area of the pyramid: "))
height = float(input("Enter the height of the pyramid: "))

area = calculate_pyramid_area(base_area, height)

print(f"The area of the pyramid is: {area}")
