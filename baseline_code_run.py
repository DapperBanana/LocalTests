
def even_fibonacci_sum(limit):
    a, b = 1, 2
    even_fibonacci_sum = 0
    
    while b <= limit:
        if b % 2 == 0:
            even_fibonacci_sum += b
        a, b = b, a + b
        
    return even_fibonacci_sum

limit = int(input("Enter the limit for Fibonacci numbers: "))
result = even_fibonacci_sum(limit)
print(f"The sum of all even Fibonacci numbers up to {limit} is: {result}")
