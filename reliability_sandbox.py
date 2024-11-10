
def convert_base(number, from_base, to_base):
    if from_base == 10:
        return decimal_to_base(number, to_base)
    else:
        return base_to_decimal(number, from_base, to_base)

def decimal_to_base(number, base):
    if base == 10:
        return number
    result = ''
    while number > 0:
        remainder = number % base
        result = str(remainder) + result
        number //= base
    return int(result)

def base_to_decimal(number, from_base, to_base):
    decimal_number = 0
    power = 0
    while number > 0:
        digit = number % 10
        decimal_number += digit * (from_base ** power)
        number //= 10
        power += 1
    return decimal_to_base(decimal_number, to_base)

# Test the function
number = 1101
from_base = 2
to_base = 10
print(f'Converting {number} from base {from_base} to base {to_base}: {convert_base(number, from_base, to_base)}')
