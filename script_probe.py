
def decimal_to_binary(decimal_num):
    if decimal_num < 0:
        return "Invalid input. Please enter a positive integer."
    
    binary_num = bin(decimal_num)[2:]
    return binary_num

decimal_num = int(input("Enter a decimal number: "))
binary_num = decimal_to_binary(decimal_num)
print(f"The binary representation of {decimal_num} is {binary_num}")
