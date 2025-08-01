
def sum_of_digits(num):
    while num > 9:
        sum_digits = sum(int(digit) for digit in str(num))
        num = sum_digits
    return num

num = int(input("Enter a number: "))
result = sum_of_digits(num)
print("The sum of the digits of the number until it becomes a single-digit number is:", result)
