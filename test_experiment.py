
def is_perfect_digital_invariant(num):
    num_str = str(num)
    reversed_num_str = num_str[::-1]
    if num_str == reversed_num_str:
        return True
    else:
        return False

# Test the function
num = 12321
if is_perfect_digital_invariant(num):
    print(f"{num} is a perfect digital invariant number.")
else:
    print(f"{num} is not a perfect digital invariant number.")
