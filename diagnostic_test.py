
def decimal_to_binary(decimal_num):
    binary_num = bin(decimal_num)[2:]
    return binary_num

decimal_number = int(input("Enter a decimal number: "))
binary_number = decimal_to_binary(decimal_number)

print(f"The binary representation of {decimal_number} is: {binary_number}")
