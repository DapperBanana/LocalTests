
from fractions import Fraction

def decimal_to_fraction(decimal_num):
    fraction = Fraction(decimal_num).limit_denominator()
    return fraction

decimal_num = float(input("Enter a decimal number: "))
fraction = decimal_to_fraction(decimal_num)

print(f"The fraction of {decimal_num} is {fraction}")
