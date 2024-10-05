
def convert_base(number, from_base, to_base):
    return int(str(number), from_base) if to_base == 10 else str(int(str(number), from_base)).lstrip('0').upper()

number = input("Enter the number to convert: ")
from_base = int(input("Enter the base of the number: "))
to_base = int(input("Enter the base to convert to: "))

converted_number = convert_base(number, from_base, to_base)

print(f"The number {number} in base {from_base} is {converted_number} in base {to_base}")
