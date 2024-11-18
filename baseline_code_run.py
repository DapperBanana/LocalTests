
def is_narcissistic_number(num):
    # Convert the number to a string to iterate through each digit
    num_str = str(num)
    num_length = len(num_str)
    
    # Calculate the sum of each digit raised to the power of the number of digits
    result = 0
    for digit in num_str:
        result += int(digit) ** num_length
    
    # Check if the sum is equal to the original number
    if result == num:
        return True
    else:
        return False

# Test the function with some example numbers
num1 = 153
num2 = 370
num3 = 9474

if is_narcissistic_number(num1):
    print(f"{num1} is a narcissistic number")
else:
    print(f"{num1} is not a narcissistic number")

if is_narcissistic_number(num2):
    print(f"{num2} is a narcissistic number")
else:
    print(f"{num2} is not a narcissistic number")

if is_narcissistic_number(num3):
    print(f"{num3} is a narcissistic number")
else:
    print(f"{num3} is not a narcissistic number")
