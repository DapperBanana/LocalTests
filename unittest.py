
def even_fib_sum(limit):
    fib_sum = 0
    a, b = 1, 2
    
    while b <= limit:
        if b % 2 == 0:
            fib_sum += b
        
        a, b = b, a + b
    
    return fib_sum

limit = int(input("Enter the limit: "))
sum_even_fib = even_fib_sum(limit)
print("Sum of even Fibonacci numbers up to", limit, "is:", sum_even_fib)
