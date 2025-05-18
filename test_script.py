
def trapezoidal_prism_area(base1, base2, height, prism_height):
    # Calculate the area of the trapezoidal base
    trapezoidal_base_area = 0.5 * (base1 + base2) * height
    
    # Calculate the lateral area of the prism
    lateral_area = (base1 + base2) * prism_height
    
    # Calculate the total surface area of the trapezoidal prism
    total_area = 2 * trapezoidal_base_area + lateral_area
    
    return total_area

base1 = float(input("Enter the length of the first base of the trapezoid: "))
base2 = float(input("Enter the length of the second base of the trapezoid: "))
height = float(input("Enter the height of the trapezoid: "))
prism_height = float(input("Enter the height of the prism: "))

area = trapezoidal_prism_area(base1, base2, height, prism_height)
print(f"The total surface area of the trapezoidal prism is: {area}")
