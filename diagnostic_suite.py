
def convert_base(number, current_base, target_base):
    base10_num = int(number, current_base)
    target_num = ''
    
    while base10_num > 0:
        remainder = base10_num % target_base
        target_num = str(remainder) + target_num
        base10_num //= target_base
    
    return target_num


number = input("Enter the number you want to convert: ")
current_base = int(input("Enter the base of the number: "))
target_base = int(input("Enter the target base: "))

converted_number = convert_base(number, current_base, target_base)

print(f"The number {number} in base {current_base} is equal to {converted_number} in base {target_base}.")
