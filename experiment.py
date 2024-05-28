
def is_harshad_number(num):
    # Calculate the sum of digits
    sum_digits = sum(int(digit) for digit in str(num))
    
    # Check if the number is divisible by the sum of its digits
    if num % sum_digits == 0:
        return True
    else:
        return False

# Take user input
num = int(input("Enter a number: "))

# Check if the number is a Harshad number
if is_harshad_number(num):
    print(f"{num} is a Harshad number.")
else:
    print(f"{num} is not a Harshad number.")
