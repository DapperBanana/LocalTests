
def sum_of_digits(num):
    total = 0
    for digit in str(num):
        total += int(digit)
    return total

num = int(input("Enter a number: "))
sum_of_digits = sum_of_digits(num)
print("Sum of digits in", num, "is:", sum_of_digits)
