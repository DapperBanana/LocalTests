
def is_harshad_number(num):
    sum_digits = 0
    for digit in str(num):
        sum_digits += int(digit)
    return num % sum_digits == 0

# Test the function
num = int(input("Enter a number: "))
if is_harshad_number(num):
    print(f"{num} is a Harshad (Niven) number.")
else:
    print(f"{num} is not a Harshad (Niven) number.")
