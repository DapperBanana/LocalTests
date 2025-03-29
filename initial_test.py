
from fractions import Fraction

def decimal_to_fraction(decimal):
    fraction = Fraction(decimal).limit_denominator()
    return fraction

decimal_number = 3.14
fraction = decimal_to_fraction(decimal_number)

print(f'The fraction form of the decimal number {decimal_number} is {fraction}')
