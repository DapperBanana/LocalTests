
def is_perfect_digital_invariant(num):
    num_str = str(num)
    total_sum = 0
    
    for digit in num_str:
        total_sum += int(digit)
    
    product = 1
    for digit in num_str:
        product *= int(digit)
    
    return total_sum * product == num


num = int(input("Enter a number: "))

if is_perfect_digital_invariant(num):
    print(f"{num} is a perfect digital invariant.")
else:
    print(f"{num} is not a perfect digital invariant.")
