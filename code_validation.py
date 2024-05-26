
from fractions import Fraction

def decimal_to_fraction(decimal):
    f = Fraction(decimal).limit_denominator()
    return f

# Take user input for the decimal number
decimal_num = float(input("Enter a decimal number: "))

# Convert the decimal number to a fraction
fraction = decimal_to_fraction(decimal_num)

print(f"The fraction representation of {decimal_num} is: {fraction}")
