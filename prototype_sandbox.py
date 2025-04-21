
def decimal_to_binary(decimal_num):
    return bin(decimal_num).replace("0b", "")

decimal_num = int(input("Enter a decimal number: "))
binary_num = decimal_to_binary(decimal_num)

print(f"The binary representation of {decimal_num} is {binary_num}")
