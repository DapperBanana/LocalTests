
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    return binary

decimal_number = int(input("Enter a decimal number: "))
binary_number = decimal_to_binary(decimal_number)

print(f"The binary representation of {decimal_number} is: {binary_number}")
