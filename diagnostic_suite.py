
def convert_base(num, from_base, to_base):
    if from_base == to_base:
        return num

    if from_base == 10:
        return decimal_to_base(num, to_base)

    decimal_num = base_to_decimal(num, from_base)
    return decimal_to_base(decimal_num, to_base)

def base_to_decimal(num, base):
    decimal_num = 0
    power = 0
    
    while num > 0:
        digit = num % 10
        decimal_num += digit * (base ** power)
        num //= 10
        power += 1

    return decimal_num

def decimal_to_base(num, base):
    result = ""
    
    while num > 0:
        digit = num % base
        result += str(digit)
        num //= base
    
    return int(result[::-1])

# Test the program
num = 101010
from_base = 2
to_base = 10

converted_num = convert_base(num, from_base, to_base)
print(f"{num} base {from_base} is equivalent to {converted_num} base {to_base}")
