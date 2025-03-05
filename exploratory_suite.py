
def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

number = int(input("Enter a number: "))
result = sum_of_digits(number)
print(f"The sum of digits in {number} is: {result}")
