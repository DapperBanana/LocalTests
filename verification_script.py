
fib_cache = {}

def fibonacci(n):
    if n in fib_cache:
        return fib_cache[n]
    
    if n <= 1:
        fib_cache[n] = n
        return n
    
    fib_cache[n] = fibonacci(n-1) + fibonacci(n-2)
    return fib_cache[n]

n = int(input("Enter a number: "))
print(f"The {n}th term of the Fibonacci sequence is: {fibonacci(n)}")
