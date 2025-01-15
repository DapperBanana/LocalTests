
def decimal_to_binary(decimal_num):
    binary_num = bin(decimal_num)
    return binary_num[2:]

#Taking input from user
decimal_num = int(input("Enter a decimal number: "))

binary_num = decimal_to_binary(decimal_num)
print(f"The binary representation of {decimal_num} is {binary_num}")
