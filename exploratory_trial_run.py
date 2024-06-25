
def calculate_pyramid_area(base_area, height):
    # Calculate the area of the pyramid using the formula (1/3) * base_area * height
    pyramid_area = (1/3) * base_area * height
    return pyramid_area

base_area = float(input("Enter the base area of the pyramid: "))
height = float(input("Enter the height of the pyramid: "))

pyramid_area = calculate_pyramid_area(base_area, height)
print("The area of the pyramid is: ", pyramid_area)
