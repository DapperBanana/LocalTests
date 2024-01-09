
def convert_base(number, from_base, to_base):
    # Convert the number to decimal first
    decimal_number = int(number, from_base)

    # Convert the decimal number to the desired base
    if to_base == 10:
        return str(decimal_number)

    converted_number = ""
    while decimal_number > 0:
        remainder = decimal_number % to_base

        # Use letters A-F for bases larger than 10
        if remainder >= 10:
            converted_number += chr(ord('A') + remainder - 10)
        else:
            converted_number += str(remainder)

        decimal_number = decimal_number // to_base

    # Reverse the converted number and return it as string
    return converted_number[::-1]


# Test the function
number = input("Enter the number to convert: ")
from_base = int(input("Enter the base of the number: "))
to_base = int(input("Enter the base to convert to: "))

converted_number = convert_base(number, from_base, to_base)
print("Converted number:", converted_number)
