
def calculate_cube_surface_area(side_length):
    surface_area = 6 * (side_length ** 2)
    return surface_area

side_length = float(input("Enter the side length of the cube: "))
surface_area = calculate_cube_surface_area(side_length)
print(f"The surface area of the cube with side length {side_length} is {surface_area}")
