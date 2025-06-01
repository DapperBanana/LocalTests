
def is_perfect_digital_invariant(num):
    num_str = str(num)
    total = 0
    
    for digit in num_str:
        total += int(digit)
    
    if num % total == 0:
        return True
    else:
        return False

# Test the function with a few examples
print(is_perfect_digital_invariant(18))  # Output: True (1 + 8 = 9, 18 % 9 == 0)
print(is_perfect_digital_invariant(23))  # Output: False (2 + 3 = 5, 23 % 5 != 0)
print(is_perfect_digital_invariant(36))  # Output: False (3 + 6 = 9, 36 % 9 == 0)
