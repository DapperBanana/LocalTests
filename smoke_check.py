
def sum_of_digits(number):
    while number > 9:
        temp_sum = 0
        while number:
            temp_sum += number % 10
            number = number // 10
        number = temp_sum
    return number

num = int(input("Enter a number: "))
result = sum_of_digits(num)

print(f"The sum of the digits of the number until it becomes a single-digit number is: {result}")
