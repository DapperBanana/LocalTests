
import math

def decimal_to_fraction(decimal):
    precision = len(str(decimal).split('.')[1])
    numerator = int(decimal * 10**precision)
    denominator = 10**precision

    gcd = math.gcd(numerator, denominator)
    numerator //= gcd
    denominator //= gcd

    return f"{numerator}/{denominator}"

# Test the function
decimal = 3.25
fraction = decimal_to_fraction(decimal)
print(f"The fraction representation of {decimal} is: {fraction}")
