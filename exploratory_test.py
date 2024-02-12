
def is_harshad_number(num):
    # Calculate the sum of the digits
    digit_sum = sum(int(digit) for digit in str(num))
    
    # Check if the number is divisible by the sum of its digits
    return num % digit_sum == 0

# Test the program with some example numbers
numbers = [18, 21, 44, 200, 202, 108, 109]

for num in numbers:
    if is_harshad_number(num):
        print(num, "is a Harshad number")
    else:
        print(num, "is not a Harshad number")
