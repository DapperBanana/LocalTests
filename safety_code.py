
def convert_base(number, base_in, base_out):
    # Convert number to decimal first
    decimal_num = 0
    power = len(str(number)) - 1

    for digit in str(number):
        decimal_num += int(digit) * base_in**power
        power -= 1

    # Convert decimal number to the desired base
    result = ''
    while decimal_num > 0:
        remainder = decimal_num % base_out
        result = str(remainder) + result
        decimal_num = decimal_num // base_out

    return result

number = input("Enter the number to convert: ")
base_in = int(input("Enter the base of the input number: "))
base_out = int(input("Enter the base to convert to: "))

result = convert_base(number, base_in, base_out)
print(f"The number {number} in base {base_in} is {result} in base {base_out}.")
