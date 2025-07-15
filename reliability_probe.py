
def is_harshad_number(num):
    sum_of_digits = sum(int(i) for i in str(num))
    if num % sum_of_digits == 0:
        return True
    return False

num = int(input("Enter a number: "))
if is_harshad_number(num):
    print(f"{num} is a Harshad number.")
else:
    print(f"{num} is not a Harshad number.")
