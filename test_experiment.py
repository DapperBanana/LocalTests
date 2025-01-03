
def is_perfect_digital_invariant(num):
    digits = [int(d) for d in str(num)]
    sum_of_digits = sum(digits)

    product_of_digits = 1
    for digit in digits:
        product_of_digits *= digit

    if sum_of_digits * product_of_digits == num:
        return True
    else:
        return False

# Test the program
num = 1230
if is_perfect_digital_invariant(num):
    print(f"{num} is a perfect digital invariant.")
else:
    print(f"{num} is not a perfect digital invariant.")
