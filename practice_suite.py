
def is_perfect_digital_invariant(num):
    # Convert the number to a string to iterate through each digit
    num_str = str(num)
    
    # Initialize a variable to keep track of the sum of squares of digits
    sum_sq = 0
    
    # Iterate through each digit in the number and calculate the sum of squares
    for digit in num_str:
        digit = int(digit)
        sum_sq += digit ** 2
    
    # Check if the sum of squares is equal to the original number
    if sum_sq == num:
        return True
    else:
        return False

# Test the program with some numbers
print(is_perfect_digital_invariant(19))  # False
print(is_perfect_digital_invariant(28))  # True
