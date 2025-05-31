
def sum_of_digits(n):
    if n <= 0:
        return 0
    
    sum_of_digits = 0
    while n > 0:
        sum_of_digits += n % 10
        n = n // 10
    
    if sum_of_digits < 10:
        return sum_of_digits
    else:
        return sum_of_digits(sum_of_digits)

num = int(input("Enter a number: "))
result = sum_of_digits(num)
print("Sum of digits until single-digit number:", result)
