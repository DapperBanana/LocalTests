
def calculate_digit_sum(num):
    while num >= 10:
        sum_of_digits = 0
        while num > 0:
            digit = num % 10
            sum_of_digits += digit
            num = num // 10
        num = sum_of_digits
    return num

number = int(input("Enter a number: "))
result = calculate_digit_sum(number)
print("Sum of digits until it becomes a single-digit number:", result)
