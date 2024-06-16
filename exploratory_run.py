
def is_harshad(num):
    if num <= 0:
        return False

    digits_sum = sum(int(digit) for digit in str(num))
    return num % digits_sum == 0

num = int(input("Enter a number: "))
if is_harshad(num):
    print(f"{num} is a Harshad number")
else:
    print(f"{num} is not a Harshad number")
