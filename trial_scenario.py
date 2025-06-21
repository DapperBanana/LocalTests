
def decimal_to_binary(decimal_number):
    binary_number = bin(decimal_number)[2:]
    return binary_number

if __name__ == "__main__":
    decimal_number = int(input("Enter a decimal number: "))
    binary_number = decimal_to_binary(decimal_number)
    print(f"The binary representation of {decimal_number} is: {binary_number}")
