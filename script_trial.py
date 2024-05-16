
def even_fibonacci_sum(limit):
    fib_sum = 0
    a, b = 1, 1
    while b <= limit:
        if b % 2 == 0:
            fib_sum += b
        a, b = b, a + b
    return fib_sum

limit = int(input("Enter the limit: "))
result = even_fibonacci_sum(limit)
print(f"The sum of all even Fibonacci numbers up to {limit} is: {result}")
