
def convert_base(number, from_base, to_base):
    if from_base == to_base:
        return number

    # Convert to decimal first
    decimal_value = 0
    power = 0
    for digit in reversed(str(number)):
        decimal_value += int(digit) * (from_base ** power)
        power += 1

    # Convert decimal to the desired base
    result = ""
    while decimal_value > 0:
        remainder = decimal_value % to_base
        result = str(remainder) + result
        decimal_value //= to_base

    return result

# Test the function
number = "1011"
from_base = 2
to_base = 10
result = convert_base(number, from_base, to_base)
print(f"{number} in base {from_base} is {result} in base {to_base}")

number = 15
from_base = 10
to_base = 2
result = convert_base(number, from_base, to_base)
print(f"{number} in base {from_base} is {result} in base {to_base}")
