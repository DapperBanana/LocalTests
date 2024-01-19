
def sum_of_digits(n):
    # Convert the number to string
    n_str = str(n)
    
    # Initialize sum
    digits_sum = 0
    
    # Iterate over each character in the string
    for digit in n_str:
        # Add the digit to the sum
        digits_sum += int(digit)
    
    return digits_sum


# Get input from the user
number = int(input("Enter a number: "))

# Calculate the sum of digits
sum = sum_of_digits(number)

# Print the result
print("Sum of digits:", sum)
