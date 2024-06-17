
def is_perfect_digital_invariant(num):
    digit_sum = sum(int(digit) for digit in str(num))
    product =(lambda x: x* int(x))(str(num))
    
    if digit_sum * product == num:
        return True
    else:
        return False

# Test the function
num = 18
if is_perfect_digital_invariant(num):
    print(f"{num} is a perfect digital invariant")
else:
    print(f"{num} is not a perfect digital invariant")
