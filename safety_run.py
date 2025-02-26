
def convert_base(num, base):
    if base == 10:
        return int(num, 2)
    elif base == 2:
        return bin(int(num))[2:]
    elif base == 8:
        return oct(int(num))[2:]
    elif base == 16:
        return hex(int(num))[2:]
    else:
        return "Invalid base"

num = input("Enter the number you want to convert: ")
current_base = int(input("Enter the current base of the number (2, 8, 10, or 16): "))
new_base = int(input("Enter the base you want to convert to (2, 8, 10, or 16): "))

result = convert_base(num, current_base)
converted_num = convert_base(result, new_base)

print(f"The number {num} in base {current_base} is equal to {converted_num} in base {new_base}")
