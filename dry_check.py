
def is_harshad_number(num):
    sum_of_digits = sum(int(digit) for digit in str(num))
    return num % sum_of_digits == 0

# Test cases
print(is_harshad_number(18))  # True (18 is divisible by the sum of its digits: 1 + 8 = 9)
print(is_harshad_number(21))  # False (21 is not divisible by the sum of its digits: 2 + 1 = 3)
print(is_harshad_number(202)) # True (202 is divisible by the sum of its digits: 2 + 0 + 2 = 4)
