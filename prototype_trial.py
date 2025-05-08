
def sum_of_digits(num):
    while num > 9:
        sum_num = 0
        while num:
            sum_num += num % 10
            num //= 10
        num = sum_num
    return num

num = int(input("Enter a number: "))
result = sum_of_digits(num)
print("Sum of digits until it becomes a single-digit number:", result)
