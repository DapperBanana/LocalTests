
def is_harshad_number(num):
    # Compute the sum of the digits of the number
    sum_of_digits = sum(int(digit) for digit in str(num))

    # Check if the number is divisible by the sum of its digits
    return num % sum_of_digits == 0

# Test the function
num = int(input("Enter a number: "))
if is_harshad_number(num):
    print(num, "is a Harshad (Niven) number")
else:
    print(num, "is not a Harshad (Niven) number")
