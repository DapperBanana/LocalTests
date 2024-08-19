
def convert_base(num, base_in, base_out):
    if base_in == base_out:
        return num
    
    if base_in == 10:
        return base_converter(num, base_out)
    else:
        decimal_num = base_converter(num, 10)
        return base_converter(decimal_num, base_out)

def base_converter(num, base):
    if base == 10:
        return int(num)
    
    result = ''
    while num > 0:
        remainder = num % base
        result = str(remainder) + result
        num = num // base
    
    return result

num = input("Enter the number: ")
base_in = int(input("Enter the base of the number: "))
base_out = int(input("Enter the base to convert to: "))

result = convert_base(num, base_in, base_out)
print(f"The number {num} in base {base_in} would be {result} in base {base_out}.")
