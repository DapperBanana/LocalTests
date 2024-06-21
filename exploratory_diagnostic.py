
def convert_num_to_decimal(number, base):
    decimal_num = 0
    power = 0
    while number > 0:
        digit = number % 10
        decimal_num += digit * (base ** power)
        power += 1
        number //= 10
    return decimal_num

def convert_decimal_to_num(decimal_num, base):
    result = ""
    while decimal_num > 0:
        remainder = decimal_num % base
        result = str(remainder) + result
        decimal_num //= base
    return result

def main():
    number = int(input("Enter the number to convert: "))
    base_from = int(input("Enter the base of the number to convert from: "))
    base_to = int(input("Enter the base of the number to convert to: "))
    
    decimal_num = convert_num_to_decimal(number, base_from)
    converted_num = convert_decimal_to_num(decimal_num, base_to)
    
    print(f"The number {number} in base {base_from} is equal to {converted_num} in base {base_to}.")

if __name__ == "__main__":
    main()
