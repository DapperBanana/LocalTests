
def is_narcissistic_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    total = 0
    
    for digit in num_str:
        total += int(digit) ** num_digits
    
    return total == number

number = int(input("Enter a number to check if it is a narcissistic number: "))
if is_narcissistic_number(number):
    print(f"{number} is a narcissistic number.")
else:
    print(f"{number} is not a narcissistic number.")
