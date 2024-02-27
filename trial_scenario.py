
import fractions

def decimal_to_fraction(decimal):
    return fractions.Fraction(decimal).limit_denominator()

decimal = float(input("Enter a decimal number: "))
fraction = decimal_to_fraction(decimal)

print(f"The fraction representation of {decimal} is: {fraction}")
