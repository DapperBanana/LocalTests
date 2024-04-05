
def decimal_to_binary(decimal_num):
    if decimal_num < 0:
        return "Please enter a positive integer."
    elif decimal_num == 0:
        return "0"
    else:
        binary_num = ""
        while decimal_num > 0:
            remainder = decimal_num % 2
            binary_num = str(remainder) + binary_num
            decimal_num = decimal_num // 2
        return binary_num

# Input from user
decimal_input = int(input("Enter a decimal number: "))
binary_output = decimal_to_binary(decimal_input)
print(f"The binary representation of {decimal_input} is: {binary_output}")
