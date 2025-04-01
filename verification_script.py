
def is_perfect_digital_invariant(num):
    num_str = str(num)
    total = 0
    for digit in num_str:
        total += int(digit)**int(digit)
    
    return total == num

num = int(input("Enter a number: "))
if is_perfect_digital_invariant(num):
    print(f"{num} is a perfect digital invariant.")
else:
    print(f"{num} is not a perfect digital invariant.")
