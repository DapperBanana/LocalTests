
def is_harshad_number(number):
    sum_of_digits = sum([int(digit) for digit in str(number)])
    return number % sum_of_digits == 0

number = int(input("Enter a number: "))
if is_harshad_number(number):
    print(f"{number} is a Harshad number.")
else:
    print(f"{number} is not a Harshad number.")
