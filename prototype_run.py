
def sum_digits(num):
    while num >= 10:
        total = 0
        while num > 0:
            total += num % 10
            num = num // 10
        num = total
    return num

number = int(input("Enter a number: "))
result = sum_digits(number)
print("The sum of the digits of the number is:", result)
