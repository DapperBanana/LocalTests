
def sum_digits(num):
    if num < 10:
        return num
    else:
        total = sum([int(digit) for digit in str(num)])  # Convert number to string, then each character to integer and sum
        return sum_digits(total)

num = int(input("Enter a number: "))
result = sum_digits(num)
print("Sum of digits until it becomes a single-digit number:", result)
