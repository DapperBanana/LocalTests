
def convert_base(number, current_base, target_base):
    # Convert the number to decimal if the current base is not 10
    if current_base != 10:
        decimal_number = int(str(number), current_base)
    else:
        decimal_number = number
    
    # Convert the decimal number to the target base
    if target_base == 2:
        return bin(decimal_number)[2:]
    elif target_base == 8:
        return oct(decimal_number)[2:]
    elif target_base == 10:
        return str(decimal_number)
    elif target_base == 16:
        return hex(decimal_number)[2:]
    else:
        return "Invalid target base"

number = int(input("Enter the number to convert: "))
current_base = int(input("Enter the current base of the number (2, 8, 10, or 16): "))
target_base = int(input("Enter the target base for conversion (2, 8, 10, or 16): "))

result = convert_base(number, current_base, target_base)
print(f"The number {number} in base {current_base} is equivalent to {result} in base {target_base}.")
