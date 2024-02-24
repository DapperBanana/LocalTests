
def even_fibonacci_sum(limit):
    # Initialize variables for the first two Fibonacci numbers
    fib1, fib2 = 1, 1
    even_sum = 0

    # Loop until the Fibonacci number exceeds the limit
    while fib2 <= limit:
        if fib2 % 2 == 0:
            even_sum += fib2
        
        fib1, fib2 = fib2, fib1 + fib2

    return even_sum

limit = int(input("Enter the limit for Fibonacci numbers: "))
result = even_fibonacci_sum(limit)
print(f"The sum of all even Fibonacci numbers up to {limit} is: {result}")
