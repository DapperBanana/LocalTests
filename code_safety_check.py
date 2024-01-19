
def is_harshad_number(number):
    # Check if the number is divisible by the sum of its digits
    sum_of_digits = sum(int(digit) for digit in str(number))
    return number % sum_of_digits == 0

# Test the program
number = int(input("Enter a number: "))
if is_harshad_number(number):
    print(number, "is a Harshad (Niven) number.")
else:
    print(number, "is not a Harshad (Niven) number.")
