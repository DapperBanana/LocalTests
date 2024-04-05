
def is_harshad_number(n):
    sum_of_digits = sum(int(digit) for digit in str(n))
    return n % sum_of_digits == 0

number = int(input("Enter a number: "))

if is_harshad_number(number):
    print(f"{number} is a Harshad (Niven) number")
else:
    print(f"{number} is not a Harshad (Niven) number")
