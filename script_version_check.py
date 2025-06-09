
def sum_of_digits(n):
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return n

num = int(input("Enter a number: "))
result = sum_of_digits(num)
print("Sum of digits until it becomes a single-digit number:", result)
