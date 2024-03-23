
def even_fibonacci_sum(limit):
    fib1, fib2 = 1, 2
    total = 0
    
    while fib2 <= limit:
        if fib2 % 2 == 0:
            total += fib2
        
        fib1, fib2 = fib2, fib1 + fib2
        
    return total

limit = int(input("Enter the limit: "))
result = even_fibonacci_sum(limit)
print(f"The sum of all even Fibonacci numbers up to {limit} is: {result}")
