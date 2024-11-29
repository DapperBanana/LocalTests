
def is_perfect_digital_invariant(num):
    str_num = str(num)
    total = 0
    for digit in str_num:
        total += int(digit) ** int(digit)
    
    return total == num

# Test the function
num = 89
if is_perfect_digital_invariant(num):
    print(f"{num} is a perfect digital invariant.")
else:
    print(f"{num} is not a perfect digital invariant.")
