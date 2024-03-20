
def is_perfect_digital_invariant(num):
    num_str = str(num)
    
    total = 0
    for digit in num_str:
        total += int(digit)
    
    if num % total == 0:
        return True
    else:
        return False

num = int(input("Enter a number: "))

if is_perfect_digital_invariant(num):
    print(f"{num} is a perfect digital invariant.")
else:
    print(f"{num} is not a perfect digital invariant.")
