
def calculate_pyramid_area(base_area, height):
    """
    Function to calculate the area of a pyramid given its base area and height.
    Formula: area = (base_area + (0.5 * base_area) * height) / 2
    """
    area = (base_area + (0.5 * base_area) * height) / 2
    return area

# Input base area and height from user
base_area = float(input("Enter the base area of the pyramid: "))
height = float(input("Enter the height of the pyramid: "))

# Calculate the area of the pyramid
pyramid_area = calculate_pyramid_area(base_area, height)

# Display the result
print(f"The area of the pyramid with base area {base_area} and height {height} is: {pyramid_area}")
