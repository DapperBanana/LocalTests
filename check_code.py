
def sum_of_digits(num):
    while num >= 10:
        total = 0
        while num > 0:
            total += num % 10
            num = num // 10
        num = total
    return num

number = int(input("Enter a number: "))
result = sum_of_digits(number)
print(f"The sum of the digits of the number until it becomes a single-digit number is: {result}")
