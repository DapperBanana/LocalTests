
def pyramid_area(base_area, height):
    # Calculate the area of the pyramid using the formula: base area + (0.5 * base perimeter * slant height)
    base_perimeter = 4 * (base_area ** 0.5)
    slant_height = ((base_perimeter ** 2) + (4 * (height ** 2))) ** 0.5
    area = base_area + (0.5 * base_perimeter * slant_height)
    
    return area

base_area = float(input("Enter the base area of the pyramid: "))
height = float(input("Enter the height of the pyramid: "))

result = pyramid_area(base_area, height)
print("The area of the pyramid is:", result)
