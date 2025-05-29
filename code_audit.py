
def calculate_pyramid_area(base_area, height):
    # Calculate the area of the pyramid
    pyramid_area = (base_area + (base_area * 4)) * (height / 3)
    return pyramid_area

if __name__ == "__main__":
    base_area = float(input("Enter the base area of the pyramid: "))
    height = float(input("Enter the height of the pyramid: "))
    
    area = calculate_pyramid_area(base_area, height)
    print(f"The area of the pyramid is: {area}")
