
# Function to calculate the area of a pyramid
def calculate_pyramid_area(base_area, height):
    pyramid_area = (base_area * height) / 3
    return pyramid_area

# Get the base area from the user
base_area = float(input("Enter the base area of the pyramid: "))

# Get the height from the user
height = float(input("Enter the height of the pyramid: "))

# Calculate the area of the pyramid
area = calculate_pyramid_area(base_area, height)

# Print the area of the pyramid
print("The area of the pyramid is", area)
