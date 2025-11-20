
def even_fibonacci_sum(limit):
    first = 1
    second = 2
    total = 0
    
    while second <= limit:
        if second % 2 == 0:
            total += second
        
        next_fib = first + second
        first = second
        second = next_fib
    
    return total

limit = int(input("Enter the limit: "))
result = even_fibonacci_sum(limit)
print("Sum of even Fibonacci numbers up to", limit, "is:", result)
