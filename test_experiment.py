
def sum_of_digits(num):
    while num > 9:
        sum_digits = 0
        while num != 0:
            sum_digits += num % 10
            num = num // 10
        num = sum_digits
    return num

num = int(input("Enter a number: "))
result = sum_of_digits(num)
print("Sum of digits until it becomes a single-digit number: ", result)
