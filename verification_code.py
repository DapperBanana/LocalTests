
def is_perfect_digital_invariant(num):
    num_str = str(num)
    total = sum([int(digit)**i for i, digit in enumerate(num_str, 1)])
    return total == num

# Test the program with some sample numbers
num1 = 175
num2 = 9474

if is_perfect_digital_invariant(num1):
    print(f"{num1} is a perfect digital invariant")
else:
    print(f"{num1} is not a perfect digital invariant")

if is_perfect_digital_invariant(num2):
    print(f"{num2} is a perfect digital invariant")
else:
    print(f"{num2} is not a perfect digital invariant")
