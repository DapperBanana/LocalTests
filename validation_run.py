
def is_harshad_number(num):
    digits_sum = sum([int(digit) for digit in str(num)])
    return num % digits_sum == 0

# Test the function with some numbers
print(is_harshad_number(18))  # Output: True
print(is_harshad_number(19))  # Output: False
print(is_harshad_number(202))  # Output: True
