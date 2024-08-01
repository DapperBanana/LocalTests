
def sum_digits(num):
    while num > 9:
        num = sum(int(digit) for digit in str(num))
    return num

number = int(input("Enter a number: "))
result = sum_digits(number)
print("The sum of the digits of the number until it becomes a single-digit number is:", result)
