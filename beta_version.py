
def even_fibonacci_sum(limit):
    fib1 = 1
    fib2 = 2
    even_sum = 0
    
    while fib2 <= limit:
        if fib2 % 2 == 0:
            even_sum += fib2
        
        fib1, fib2 = fib2, fib1 + fib2
    
    return even_sum

# Input limit from user
limit = int(input("Enter a limit: "))

result = even_fibonacci_sum(limit)
print("The sum of all even Fibonacci numbers up to", limit, "is:", result)
