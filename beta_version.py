
def decimal_to_binary(decimal):
    # Using built-in bin() function to convert decimal to binary
    binary = bin(decimal)[2:]
    return binary

decimal_number = int(input("Enter a decimal number: "))
binary_number = decimal_to_binary(decimal_number)
print(f"The binary representation of {decimal_number} is: {binary_number}")
