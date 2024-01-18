
def is_perfect_digital_invariant(num):
    num_str = str(num)
    length = len(num_str)
    if length <= 1:
        return True

    digit_sum = sum(int(digit) for digit in num_str)
    digit_product = 1
    for digit in num_str:
        digit_product *= int(digit)

    if digit_sum == digit_product:
        return True
    else:
        return False

# Test the program
num = int(input("Enter a number: "))
if is_perfect_digital_invariant(num):
    print(f"{num} is a perfect digital invariant.")
else:
    print(f"{num} is not a perfect digital invariant.")
