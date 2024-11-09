
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def sum_even_fibonacci(limit):
    even_sum = 0
    n = 0
    fib_num = fib(n)
    
    while fib_num <= limit:
        if fib_num % 2 == 0:
            even_sum += fib_num
        n += 1
        fib_num = fib(n)
    
    return even_sum

limit = int(input("Enter the limit for Fibonacci numbers: "))
result = sum_even_fibonacci(limit)
print("Sum of even Fibonacci numbers up to", limit, "is:", result)
