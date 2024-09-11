
def is_perfect_digital_invariant(number):
    digits = [int(d) for d in str(number)]
    
    total = sum(digits)
    product = 1
    
    for digit in digits:
        if digit != 0:
            product *= digit
    
    return product == total

number = int(input("Enter a number: "))
if is_perfect_digital_invariant(number):
    print(f"{number} is a perfect digital invariant.")
else:
    print(f"{number} is not a perfect digital invariant.")
