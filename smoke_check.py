
def calculate_area(base1, base2, height, side_length):
    # Calculate the area of the trapezoid
    trapezoid_area = (base1 + base2) * height / 2
    
    # Calculate the lateral area of the prism
    lateral_area = trapezoid_area * side_length
    
    # Calculate the total area of the prism (including the bases)
    base_area = (base1 + base2) * side_length
    total_area = 2 * trapezoid_area + base_area
    
    return lateral_area, total_area

# Example usage
base1 = 5
base2 = 8
height = 4
side_length = 10

lateral_area, total_area = calculate_area(base1, base2, height, side_length)
print("Lateral Area of the Trapezoidal Prism:", lateral_area)
print("Total Area of the Trapezoidal Prism:", total_area)
