
def is_perfect_digital_invariant(num):
    digits = [int(d) for d in str(num)]
    sum_digits = sum(digits)
    product_digits = 1
    for digit in digits:
        product_digits *= digit
    
    return sum_digits == product_digits

# Test the program
num = int(input("Enter a number: "))
if is_perfect_digital_invariant(num):
    print(num, "is a perfect digital invariant.")
else:
    print(num, "is not a perfect digital invariant.")
