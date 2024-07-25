
def is_perfect_digital_invariant(num):
    # Convert number to string to iterate over its digits
    num_str = str(num)
    
    # Calculate sum of cubes of digits
    sum_cubes = sum(int(digit)**3 for digit in num_str)
    
    # Check if sum of cubes is equal to the original number
    if sum_cubes == num:
        return True
    else:
        return False

# Input number to check
num = int(input("Enter a number: "))

# Check if number is a perfect digital invariant
if is_perfect_digital_invariant(num):
    print(f"{num} is a perfect digital invariant.")
else:
    print(f"{num} is not a perfect digital invariant.")
