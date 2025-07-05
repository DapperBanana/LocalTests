
def even_fibonacci_sum(limit):
    fib1 = 1
    fib2 = 1
    even_sum = 0
    
    while fib1 <= limit:
        if fib1 % 2 == 0:
            even_sum += fib1
        
        fib1, fib2 = fib2, fib1 + fib2

    return even_sum

limit = int(input("Enter the limit: "))
result = even_fibonacci_sum(limit)
print(f"The sum of all even Fibonacci numbers up to {limit} is: {result}")
