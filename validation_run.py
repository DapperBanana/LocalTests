
from fractions import Fraction

# Function to convert decimal number to fraction
def decimal_to_fraction(decimal):
    return Fraction(decimal).limit_denominator()

# Taking input from the user
decimal_num = float(input("Enter a decimal number: "))

# Converting decimal number to fraction
fraction_num = decimal_to_fraction(decimal_num)

print(f"The fraction representation of {decimal_num} is: {fraction_num}")
