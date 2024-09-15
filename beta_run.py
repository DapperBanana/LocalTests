
from fractions import Fraction

def decimal_to_fraction(decimal_number):
    return Fraction(decimal_number).limit_denominator()

decimal_number = float(input("Enter a decimal number: "))
fraction = decimal_to_fraction(decimal_number)

print(f"The fraction representation of {decimal_number} is: {fraction}")
