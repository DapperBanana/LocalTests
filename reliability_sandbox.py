
def is_harshad_number(num):
    sum_digits = sum(int(digit) for digit in str(num))
    return num % sum_digits == 0

num = int(input("Enter a number: "))

if is_harshad_number(num):
    print(f"{num} is a Harshad (Niven) number.")
else:
    print(f"{num} is not a Harshad (Niven) number.")
