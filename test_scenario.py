
def is_narcissistic_number(number):
    num_str = str(number)
    num_length = len(num_str)
    
    sum_of_powers = sum(int(digit) ** num_length for digit in num_str)
    
    if sum_of_powers == number:
        return True
    else:
        return False

# Test the function
number = int(input("Enter a number: "))
if is_narcissistic_number(number):
    print(f"{number} is a narcissistic number.")
else:
    print(f"{number} is not a narcissistic number.")
