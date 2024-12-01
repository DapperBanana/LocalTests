
def is_harshad_number(number):
    # Calculate the sum of the digits
    sum_digits = sum(int(digit) for digit in str(number))
    
    # Check if the number is divisible by the sum of its digits
    if number % sum_digits == 0:
        return True
    else:
        return False

# Get input from the user
num = int(input("Enter a number: "))

# Check if the number is a Harshad number
if is_harshad_number(num):
    print(f"{num} is a Harshad (Niven) number.")
else:
    print(f"{num} is not a Harshad (Niven) number.")
