
def calculate_area(base_top, base_bottom, height, length):
    # Calculate the area of the trapezoidal base
    base_area = (base_top + base_bottom) / 2 * height

    # Calculate the area of the rectangular sides
    side_area = (base_top + base_bottom) * length

    # Calculate the total area of the trapezoidal prism
    total_area = 2 * base_area + side_area

    return total_area

# Example usage
base_top = 4
base_bottom = 6
height = 8
length = 10

area = calculate_area(base_top, base_bottom, height, length)
print("The area of the trapezoidal prism is:", area)
