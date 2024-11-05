
from fractions import Fraction

def decimal_to_fraction(decimal):
    fraction = Fraction(decimal).limit_denominator()
    return fraction

decimal = float(input("Enter a decimal number: "))
fraction = decimal_to_fraction(decimal)
print(f"The fraction representation of {decimal} is: {fraction}")
