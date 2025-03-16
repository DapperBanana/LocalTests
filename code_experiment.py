
def decimal_to_binary(decimal_num):
    binary_num = bin(decimal_num).replace("0b", "")
    return binary_num

# Get input from user
decimal_num = int(input("Enter a decimal number: "))

# Convert decimal number to binary
binary_num = decimal_to_binary(decimal_num)

# Output the binary number
print(f"The binary representation of {decimal_num} is: {binary_num}")
