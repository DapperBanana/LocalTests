
def is_narcissistic_number(num):
    # Count number of digits in the number
    num_str = str(num)
    num_digits = len(num_str)
    
    # Calculate the sum of each digit raised to the power of the total number of digits
    sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum is equal to the original number
    if sum_of_digits == num:
        return True
    else:
        return False

# Test the function with some examples
print(is_narcissistic_number(153))  # True
print(is_narcissistic_number(370))  # True
print(is_narcissistic_number(9474))  # True
print(is_narcissistic_number(123))  # False
