
def is_perfect_digital_invariant(num):
    num_str = str(num)
    num_sum = sum(int(digit) for digit in num_str)
    num_product = 1
    for digit in num_str:
        if digit != '0':
            num_product *= int(digit)
    
    return num_sum * num_product == num

# Test the function
num = int(input("Enter a number: "))
if is_perfect_digital_invariant(num):
    print(f"{num} is a perfect digital invariant.")
else:
    print(f"{num} is not a perfect digital invariant.")
