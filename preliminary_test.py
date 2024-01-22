
def is_narcissistic(num):
    # Convert the number to string for easier manipulation
    num_str = str(num)
    
    # Calculate the number of digits
    num_digits = len(num_str)
    
    # Calculate the sum of the digits raised to the power of the number of digits
    narcissistic_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the calculated sum is equal to the original number
    if narcissistic_sum == num:
        return True
    else:
        return False

# Test the function
num = int(input("Enter a number: "))
if is_narcissistic(num):
    print(num, "is a narcissistic number")
else:
    print(num, "is not a narcissistic number")
