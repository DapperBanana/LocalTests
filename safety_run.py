
def sum_of_digits(num):
    while num >= 10:
        sum_digits = 0
        while num > 0:
            sum_digits += num % 10
            num //= 10
        num = sum_digits
    return num

number = int(input("Enter a number: "))
result = sum_of_digits(number)

print("The sum of the digits of the number until it becomes a single-digit number is:", result)
