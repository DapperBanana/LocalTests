
def sum_of_digits(number):
    # Convert the number to a string to iterate over its digits
    number_str = str(number)
    
    # Create a variable to store the sum of digits
    sum_digits = 0
    
    # Iterate over each digit in the number
    for digit in number_str:
        # Convert each digit back to an integer before adding it to the sum
        sum_digits += int(digit)
    
    # Return the sum of digits
    return sum_digits

# Example usage
number = 12345
print("Sum of digits in", number, "is", sum_of_digits(number))
