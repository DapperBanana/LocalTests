
def convert_base(num, base_from, base_to):
    if base_from < 2 or base_to < 2:
        return "Base must be greater than 1"

    decimal_num = int(str(num), base_from)
    converted_num = ""
    
    while decimal_num > 0:
        remainder = decimal_num % base_to
        converted_num = str(remainder) + converted_num
        decimal_num = decimal_num // base_to
    
    return converted_num

num = input("Enter the number to convert: ")
base_from = int(input("Enter the base of the number: "))
base_to = int(input("Enter the base to convert to: "))

converted_num = convert_base(num, base_from, base_to)
print(f"The number {num} in base {base_from} is {converted_num} in base {base_to}")
