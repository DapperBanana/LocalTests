
def is_narcissistic_number(num):
    # Count the number of digits in the number
    num_str = str(num)
    num_digits = len(num_str)
    
    # Calculate the narcissistic sum of the digits raised to the power of the number of digits
    narcissistic_sum = 0
    for digit in num_str:
        narcissistic_sum += int(digit) ** num_digits
    
    # Check if the narcissistic sum is equal to the original number
    if narcissistic_sum == num:
        return True
    else:
        return False

# Test the function with some examples
print(is_narcissistic_number(153))  # True (1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153)
print(is_narcissistic_number(9474))  # True (9^4 + 4^4 + 7^4 + 4^4 = 6561 + 256 + 2401 + 256 = 9474)
print(is_narcissistic_number(123))  # False
