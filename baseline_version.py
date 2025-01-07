
def is_perfect_digital_invariant(num):
    num_str = str(num)
    digit_sum = sum(int(d) for d in num_str)
    digit_product = 1
    for d in num_str:
        digit_product *= int(d)
    return digit_sum * digit_product == num

num = int(input("Enter a number: "))
if is_perfect_digital_invariant(num):
    print(f"{num} is a perfect digital invariant.")
else:
    print(f"{num} is not a perfect digital invariant.")
