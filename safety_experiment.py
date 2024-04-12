
def decimal_to_binary(decimal):
    if decimal < 0:
        return "Invalid input. Please enter a non-negative number."
    if decimal == 0:
        return "0"
    
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    
    return binary

decimal_number = int(input("Enter a decimal number: "))
binary_number = decimal_to_binary(decimal_number)

print(f"The binary representation of {decimal_number} is: {binary_number}")
