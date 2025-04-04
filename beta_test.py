
def is_harshad_number(num):
    sum_of_digits = sum(int(digit) for digit in str(num))
    return num % sum_of_digits == 0

num = int(input("Enter a number: "))
if is_harshad_number(num):
    print(f"{num} is a Harshad number.")
else:
    print(f"{num} is not a Harshad number.")
