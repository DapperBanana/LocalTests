
def is_perfect_digital_invariant(num):
    digits = [int(digit) for digit in str(num)]
    total = sum(digits)
    
    if total * len(digits) == num:
        return True
    else:
        return False

# Test the function
num = 18
if is_perfect_digital_invariant(num):
    print(f"{num} is a perfect digital invariant.")
else:
    print(f"{num} is not a perfect digital invariant.")
