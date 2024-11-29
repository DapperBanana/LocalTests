
def even_fib_sum(limit):
    fib_1, fib_2 = 1, 2
    even_sum = 0
    
    while fib_2 <= limit:
        if fib_2 % 2 == 0:
            even_sum += fib_2
        
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    
    return even_sum

limit = int(input("Enter the limit for Fibonacci numbers: "))
result = even_fib_sum(limit)
print(f"The sum of all even Fibonacci numbers up to {limit} is: {result}")
