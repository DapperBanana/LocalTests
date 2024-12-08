
from fractions import Fraction

def decimal_to_fraction(decimal):
    return Fraction(decimal).limit_denominator()

decimal_number = 3.14159
fraction = decimal_to_fraction(decimal_number)

print(f"The fraction representation of {decimal_number} is {fraction}")
