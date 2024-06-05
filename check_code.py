
def sum_of_digits(n):
    while n >= 10:
        sum = 0
        while n > 0:
            sum += n % 10
            n //= 10
        n = sum
    return n

num = int(input("Enter a number: "))
result = sum_of_digits(num)

print("The sum of the digits of the number until it becomes a single-digit number is:", result)
