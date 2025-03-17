
def is_perfect_digital_invariant(number):
    num_str = str(number)
    total_sum = 0
    
    for digit in num_str:
        total_sum += int(digit) ** int(digit)
    
    return total_sum == number

number = int(input("Enter a number: "))
if is_perfect_digital_invariant(number):
    print(f"{number} is a perfect digital invariant.")
else:
    print(f"{number} is not a perfect digital invariant.")
