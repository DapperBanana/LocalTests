
def is_narcissistic_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    
    narcissistic_sum = 0
    for digit in num_str:
        narcissistic_sum += int(digit) ** num_digits
    
    if narcissistic_sum == num:
        return True
    else:
        return False

# Test the program with some example numbers
print(is_narcissistic_number(153))  # Output: True
print(is_narcissistic_number(370))  # Output: True
print(is_narcissistic_number(9474))  # Output: True
print(is_narcissistic_number(123))  # Output: False
