
def calculate_area(length_of_top_base, length_of_bottom_base, height, thickness):
    top_area = (length_of_top_base + length_of_bottom_base) * height / 2
    side_area = (length_of_top_base + length_of_bottom_base) * thickness
    total_area = 2 * top_area + 3 * side_area
    return total_area

length_of_top_base = float(input("Enter the length of the top base: "))
length_of_bottom_base = float(input("Enter the length of the bottom base: "))
height = float(input("Enter the height: "))
thickness = float(input("Enter the thickness: "))

area = calculate_area(length_of_top_base, length_of_bottom_base, height, thickness)
print("The area of the trapezoidal prism is:", area)
