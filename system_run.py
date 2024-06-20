
def calculate_pyramid_area(base_area, height):
    # Calculate the area of the pyramid
    area = (base_area + base_area + (base_area * height)) / 2
    return area

# Taking input from the user
base_area = float(input("Enter the base area of the pyramid: "))
height = float(input("Enter the height of the pyramid: "))

# Calculate the area of the pyramid
pyramid_area = calculate_pyramid_area(base_area, height)

print("The area of the pyramid is: ", pyramid_area)
