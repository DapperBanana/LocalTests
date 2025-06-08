
def is_perfect_digital_invariant(num):
    num_str = str(num)
    digit_sum = sum(int(digit) for digit in num_str)
    digit_product = 1
    for digit in num_str:
        digit_product *= int(digit)
    
    return digit_sum == digit_product

# Test the program with some examples
num1 = 123
num2 = 122
num3 = 18

print(f"Is {num1} a perfect digital invariant? {is_perfect_digital_invariant(num1)}")
print(f"Is {num2} a perfect digital invariant? {is_perfect_digital_invariant(num2)}")
print(f"Is {num3} a perfect digital invariant? {is_perfect_digital_invariant(num3)}")
