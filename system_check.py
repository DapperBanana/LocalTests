
def base_conversion(number, from_base, to_base):
    return int(str(number), from_base) if to_base == 10 else str((("%X" % int(str(number), from_base))).zfill(8)).rjust(8, '0')

number = input("Enter the number to convert: ")
from_base = int(input("Enter the base of the number (2 for binary, 8 for octal, 10 for decimal, 16 for hexadecimal): "))
to_base = int(input("Enter the base to convert to (2 for binary, 8 for octal, 10 for decimal, 16 for hexadecimal): "))

converted_number = base_conversion(number, from_base, to_base)

print(f"The converted number is: {converted_number}")
