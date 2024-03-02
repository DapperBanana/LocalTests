
import math

def calculate_area(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return area

def main():
    side1 = float(input("Enter the length of side 1: "))
    side2 = float(input("Enter the length of side 2: "))
    side3 = float(input("Enter the length of side 3: "))

    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        area = calculate_area(side1, side2, side3)
        print("The area of the triangle is: {:.2f}".format(area))
    else:
        print("Invalid triangle sides. Please make sure the sum of any two sides is greater than the third side.")

if __name__ == "__main__":
    main()
