
def surface_area_cube(side_length):
    surface_area = 6 * side_length ** 2
    return surface_area

side_length = float(input("Enter the side length of the cube: "))
print("The surface area of the cube is:", surface_area_cube(side_length))
