
def convert_base(number, from_base, to_base):
    """Convert a number from one base to another"""
    
    if from_base == "decimal":
        num = int(number)
    else:
        num = int(number, from_base)
    
    if to_base == "decimal":
        return str(num)
    else:
        return str(hex(num) if to_base == 16 else bin(num))

# Get user input
number = input("Enter the number to convert: ")
from_base = int(input("Enter the base of the number (2 for binary, 8 for octal, 10 for decimal, 16 for hexadecimal): "))
to_base = int(input("Enter the base to convert to (2, 8, 10, 16): "))

result = convert_base(number, from_base, to_base)
print(f"The result is: {result}")
