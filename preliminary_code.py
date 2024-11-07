
def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return '0'
    
    binary_num = ''
    
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num = str(remainder) + binary_num
        decimal_num = decimal_num // 2
    
    return binary_num

if __name__ == '__main__':
    decimal_num = int(input("Enter a decimal number: "))
    binary_num = decimal_to_binary(decimal_num)
    
    print(f"The binary representation of {decimal_num} is: {binary_num}")
