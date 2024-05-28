
def is_harshad_number(num):
    digits_sum = sum([int(digit) for digit in str(num)])
    return num % digits_sum == 0

num = int(input("Enter a number: "))
if is_harshad_number(num):
    print(num, "is a Harshad (Niven) number.")
else:
    print(num, "is not a Harshad (Niven) number.")
