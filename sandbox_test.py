
def calculate_pyramid_area(base_area, height):
    area = (base_area + (base_area**2 + 4 * base_area * height)**0.5) / 2
    return area

base_area = float(input("Enter the base area of the pyramid: "))
height = float(input("Enter the height of the pyramid: "))

pyramid_area = calculate_pyramid_area(base_area, height)
print("The area of the pyramid is: ", pyramid_area)
