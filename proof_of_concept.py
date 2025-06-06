
from fractions import Fraction

# Function to convert decimal to fraction
def decimal_to_fraction(decimal):
    return Fraction(decimal).limit_denominator()

# Main program
decimal_num = float(input("Enter a decimal number: "))
fraction_result = decimal_to_fraction(decimal_num)

print(f"The fraction equivalent of {decimal_num} is: {fraction_result}")
