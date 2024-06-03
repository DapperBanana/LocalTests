
def is_perfect_digital_invariant(num):
    num_str = str(num)
    digit_sum = sum(int(digit) for digit in num_str)
    product = 1
    for digit in num_str:
        product *= int(digit)
    
    return digit_sum * product == num

num = int(input("Enter a number: "))
if is_perfect_digital_invariant(num):
    print(f"{num} is a perfect digital invariant.")
else:
    print(f"{num} is not a perfect digital invariant.")
