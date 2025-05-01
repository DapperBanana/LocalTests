
def get_sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total
    
def get_single_digit_sum(n):
    while n > 9:
        n = get_sum_of_digits(n)
    return n

num = int(input("Enter a number: "))
result = get_single_digit_sum(num)
print(f"The sum of the digits of the number until it becomes a single-digit number is: {result}")
