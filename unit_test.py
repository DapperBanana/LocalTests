
def even_fibonacci_sum(limit):
    fib1, fib2 = 1, 2
    total_sum = 0

    while fib2 <= limit:
        if fib2 % 2 == 0:
            total_sum += fib2

        fib1, fib2 = fib2, fib1 + fib2

    return total_sum

limit = int(input("Enter the limit for Fibonacci numbers: "))
result = even_fibonacci_sum(limit)

print("Sum of even Fibonacci numbers up to", limit, "is:", result)
