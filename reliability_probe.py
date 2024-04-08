
def sum_of_digits(num):
    sum_digits = 0
    for digit in str(num):
        sum_digits += int(digit)
    return sum_digits

num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))
