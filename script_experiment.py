
def decimal_to_binary(decimal):
    binary = bin(decimal)
    return binary[2:]  # Remove the '0b' prefix in the binary representation

# Main program
decimal_num = int(input("Enter a decimal number: "))
binary_num = decimal_to_binary(decimal_num)
print(f"The binary representation of {decimal_num} is {binary_num}")
