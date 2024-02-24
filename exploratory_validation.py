
def sum_digits(number):
    sum = 0
    while number > 0:
        digit = number % 10
        sum += digit
        number = number // 10
    return sum

number = int(input("Enter a number: "))
result = sum_digits(number)
print(f"The sum of digits in the number {number} is: {result}")
