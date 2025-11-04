
def digit_sum(num):
    while num >= 10:
        temp_sum = 0
        while num > 0:
            temp_sum += num % 10
            num //= 10
        num = temp_sum
    return num

num = int(input("Enter a number: "))
result = digit_sum(num)
print(f"The sum of digits of the number until it becomes a single-digit number is: {result}")
