
def convert_base(num, base1, base2):
    if base1 == base2:
        return num
    
    if base1 == 10:
        return int(str(num), base=base2)
    
    if base2 == 10:
        return int(str(num), base=base1)
    
    decimal_num = 0
    for i, digit in enumerate(str(num)[::-1]):
        decimal_num += int(digit, base=base1) * (base1 ** i)
    
    converted_num = ""
    while decimal_num > 0:
        converted_num = str(decimal_num % base2) + converted_num
        decimal_num //= base2
    
    return int(converted_num) if base2 != 10 else converted_num

# Example usage
num = 1010
base1 = 2
base2 = 10
result = convert_base(num, base1, base2)
print(f"{num} in base {base1} is equal to {result} in base {base2}")
