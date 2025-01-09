
def is_perfect_digital_invariant(num):
    num_str = str(num)
    total = 0
    
    for digit in num_str:
        total += int(digit)
    
    if total * int(num_str[-1]) == num:
        return True
    else:
        return False

# Test the function
num = 18
if is_perfect_digital_invariant(num):
    print(f"{num} is a perfect digital invariant.")
else:
    print(f"{num} is not a perfect digital invariant.")
