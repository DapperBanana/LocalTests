
def convert_base(num, from_base, to_base):
    if from_base == to_base:
        return num
    
    if from_base == 10:
        return decimal_to_base(num, to_base)
    else:
        decimal_num = base_to_decimal(num, from_base)
        return decimal_to_base(decimal_num, to_base)

def base_to_decimal(num, base):
    decimal_num = 0
    num_str = str(num)
    for i in range(len(num_str)):
        digit = int(num_str[i])
        decimal_num += digit * (base ** (len(num_str) - i - 1))
    return decimal_num

def decimal_to_base(num, base):
    result = ''
    while num > 0:
        remainder = num % base
        result = str(remainder) + result
        num = num // base
    return result

# Test the program
num = 1010
from_base = 2
to_base = 10

converted_num = convert_base(num, from_base, to_base)
print(f"{num} in base {from_base} is {converted_num} in base {to_base}")
