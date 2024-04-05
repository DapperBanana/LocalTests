
from fractions import Fraction

def decimal_to_fraction(decimal_num):
    return Fraction(decimal_num).limit_denominator()

decimal_num = float(input("Enter a decimal number: "))
fraction = decimal_to_fraction(decimal_num)

print(f"The fraction equivalent of {decimal_num} is: {fraction}")
