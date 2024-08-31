
def is_perfect_digital_invariant(num):
    num_str = str(num)
    for digit in num_str:
        if int(digit) == 0 or num % int(digit) != 0:
            return False
            
    return set(num_str) == set(str(num * int(digit)) for digit in num_str)

# Test the function with some examples
num1 = 145
num2 = 1729

if is_perfect_digital_invariant(num1):
    print(f"{num1} is a perfect digital invariant")
else:
    print(f"{num1} is not a perfect digital invariant")

if is_perfect_digital_invariant(num2):
    print(f"{num2} is a perfect digital invariant")
else:
    print(f"{num2} is not a perfect digital invariant")
