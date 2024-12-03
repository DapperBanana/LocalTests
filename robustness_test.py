
def is_perfect_digital_invariant(number):
    str_number = str(number)
    total = 0
    for digit in str_number:
        total += int(digit)**int(digit)
    
    return total == number

# Test the function
number = int(input("Enter a number to check if it is a perfect digital invariant: "))
if is_perfect_digital_invariant(number):
    print(f"{number} is a perfect digital invariant.")
else:
    print(f"{number} is not a perfect digital invariant.")
