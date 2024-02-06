
def sum_digits(number):
    while number >= 10:
        sum = 0
        while number > 0:
            sum += number % 10  # Add the last digit to the sum
            number //= 10  # Remove the last digit
        number = sum  # Update the number with the new sum
    return number

number = int(input("Enter a number: "))
result = sum_digits(number)
print("The sum of the digits until it becomes a single-digit number is:", result)
