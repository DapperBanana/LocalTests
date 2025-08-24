
from fractions import Fraction

def decimal_to_fraction(decimal):
    return Fraction(decimal).limit_denominator()

decimal = float(input("Enter a decimal number: "))
fraction = decimal_to_fraction(decimal)

print(f"The fraction equivalent of {decimal} is: {fraction}")
