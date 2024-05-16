
def convert_base(number, from_base, to_base):
    if from_base == to_base:
        return number

    if from_base == 10:
        return decimal_to_base(number, to_base)
    elif to_base == 10:
        return base_to_decimal(number, from_base)
    else:
        decimal_number = base_to_decimal(number, from_base)
        return decimal_to_base(decimal_number, to_base)


def base_to_decimal(number, base):
    decimal_number = 0
    power = 0

    while number > 0:
        digit = number % 10
        decimal_number += digit * (base ** power)
        number //= 10
        power += 1
    
    return decimal_number

    
def decimal_to_base(number, base):
    if number == 0:
        return 0

    result = ""
    while number > 0:
        remainder = number % base
        result = str(remainder) + result
        number //= base
        
    return int(result)


number = int(input("Enter the number to convert: "))
from_base = int(input("Enter the base of the number: "))
to_base = int(input("Enter the base to convert to: "))

result = convert_base(number, from_base, to_base)
print(f"The number {number} in base {from_base} is equal to {result} in base {to_base}.")
