
def calculate_even_fibonacci_sum(limit):
    num1, num2 = 1, 2
    even_sum = 0

    while num2 <= limit:
        if num2 % 2 == 0:
            even_sum += num2
        num1, num2 = num2, num1 + num2

    return even_sum

limit = int(input("Enter the limit for Fibonacci numbers: "))
result = calculate_even_fibonacci_sum(limit)
print("The sum of all even Fibonacci numbers up to", limit, "is:", result)
