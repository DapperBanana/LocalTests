
# Function to convert a number from one base to another
def convert_number(num, base):
    if base == "binary":
        return int(num, 2)
    elif base == "decimal":
        return int(num)
    elif base == "octal":
        return int(num, 8)
    elif base == "hexadecimal":
        return int(num, 16)
    else:
        return "Invalid base provided"

# Get input from the user
num = input("Enter the number to convert: ")
current_base = input("Enter the base of the number (binary, decimal, octal, or hexadecimal): ")
new_base = input("Enter the base you want to convert to (binary, decimal, octal, or hexadecimal): ")

# Convert the number to the new base
result = convert_number(num, current_base)
if isinstance(result, int):
    new_num = "{0:x}".format(result) if new_base == "hexadecimal" else "{0:o}".format(result) if new_base == "octal" else bin(result)[2:] if new_base == "binary" else str(result)
    print(f"The number {num} in base {current_base} is equal to {new_num} in base {new_base}.")
else:
    print(result)
