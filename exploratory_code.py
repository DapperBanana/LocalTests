
def is_harshad_number(num):
    total = sum(int(digit) for digit in str(num))
    if num % total == 0:
        return True
    else:
        return False

num = int(input("Enter a number: "))
if is_harshad_number(num):
    print(num, "is a Harshad (Niven) number.")
else:
    print(num, "is not a Harshad (Niven) number.")
