
def is_harshad_number(num):
    # Convert the number to string and calculate the sum of its digits
    digit_sum = sum(int(digit) for digit in str(num))
    
    # Check if the number is divisible by the sum of its digits
    return num % digit_sum == 0

# Take input from the user
num = int(input("Enter a number: "))

# Check if the number is a Harshad number
if is_harshad_number(num):
    print(num, "is a Harshad number.")
else:
    print(num, "is not a Harshad number.")
