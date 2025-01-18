
def calculate_sum_even_fibonacci(limit):
    a, b = 1, 2
    fib_sum = 0
    
    while b <= limit:
        if b % 2 == 0:
            fib_sum += b
        
        a, b = b, a + b
    
    return fib_sum

limit = int(input("Enter the limit to calculate the sum of even Fibonacci numbers: "))
result = calculate_sum_even_fibonacci(limit)
print(f"The sum of even Fibonacci numbers up to {limit} is: {result}")
