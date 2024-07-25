
def convert_base(num, from_base, to_base):
    if from_base == "decimal":
        decimal_num = int(num)
    else:
        decimal_num = int(num, from_base)
    
    converted_num = ""
    while decimal_num > 0:
        remainder = decimal_num % to_base
        if remainder < 10:
            converted_num = str(remainder) + converted_num
        else:
            converted_num = chr(remainder + 55) + converted_num
        decimal_num = decimal_num // to_base
    
    return converted_num

# Main program
num = input("Enter the number you want to convert: ")
from_base = int(input("Enter the base of the number you entered: "))
to_base = int(input("Enter the base you want to convert to: "))

result = convert_base(num, from_base, to_base)
print(f"The number {num} in base {from_base} is equal to {result} in base {to_base}.")
