
def fibonacci_sum(limit):
    fib = [1, 2]
    while fib[-1] + fib[-2] <= limit:
        fib.append(fib[-1] + fib[-2])
    
    even_sum = 0
    for num in fib:
        if num % 2 == 0:
            even_sum += num
    
    return even_sum

limit = int(input("Enter the limit for Fibonacci numbers: "))
print(f"The sum of all even Fibonacci numbers up to {limit} is: {fibonacci_sum(limit)}")
