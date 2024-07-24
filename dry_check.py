
def convert_to_decimal(num, base):
    decimal = 0
    power = 0
    while num > 0:
        digit = num % 10
        decimal += digit * (base ** power)
        num //= 10
        power += 1
    return decimal

def convert_to_base(decimal, base):
    result = ""
    while decimal > 0:
        digit = decimal % base
        result = str(digit) + result
        decimal //= base
    return result

def main():
    num = int(input("Enter the number: "))
    from_base = int(input("Enter the base of the number: "))
    to_base = int(input("Enter the base you want to convert to: "))

    decimal = convert_to_decimal(num, from_base)
    result = convert_to_base(decimal, to_base)

    print(f"The number {num} in base {from_base} is equivalent to {result} in base {to_base}")

if __name__ == "__main__":
    main()
