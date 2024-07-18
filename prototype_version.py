
from fractions import Fraction

# Input decimal number
decimal_num = float(input("Enter a decimal number: "))

# Convert decimal number to fraction
fraction_num = Fraction(decimal_num).limit_denominator()

print("Fraction representation of the decimal number is:", fraction_num)
