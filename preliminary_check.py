
def is_harshad_number(num):
    # Check if number is positive
    if num <= 0:
        return False
    
    # Calculate sum of digits
    sum_digits = sum(int(digit) for digit in str(num))
    
    # Check if number is divisible by sum of digits
    return num % sum_digits == 0

# Test the function with some example numbers
print(is_harshad_number(18))  # True, 18 is divisible by 1 + 8 = 9
print(is_harshad_number(12))  # True, 12 is divisible by 1 + 2 = 3
print(is_harshad_number(20))  # False, 20 is not divisible by 2 + 0 = 2
print(is_harshad_number(0))   # False, 0 is not a positive number
