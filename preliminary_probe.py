
def is_narcissistic_number(num):
    digits = [int(d) for d in str(num)]
    num_digits = len(digits)
    narc_num = sum(digit ** num_digits for digit in digits)
    return num == narc_num

# Example usage
num = int(input("Enter a number: "))
if is_narcissistic_number(num):
    print(num, "is a narcissistic number.")
else:
    print(num, "is not a narcissistic number.")
