
def convert_base(num, from_base, to_base):
    if isinstance(num, int):
        num = str(num)

    base10 = 0
    for i in range(len(num)):
        base10 += int(num[::-1][i]) * (from_base ** i)

    result = ''
    while base10 > 0:
        result = str(base10 % to_base) + result
        base10 //= to_base

    return result

# Test the program
num = '101010' # Binary number
from_base = 2
to_base = 10
print(f'Binary {num} in decimal is: {convert_base(num, from_base, to_base)}')

num = '26' # Decimal number
from_base = 10
to_base = 2
print(f'Decimal {num} in binary is: {convert_base(num, from_base, to_base)}')
