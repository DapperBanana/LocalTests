
def calculate_fibonacci_sum(limit):
    a, b = 0, 1
    sum_even_fibonacci = 0
    
    while b <= limit:
        if b % 2 == 0:
            sum_even_fibonacci += b
        
        a, b = b, a + b
        
    return sum_even_fibonacci

limit = int(input("Enter the limit for Fibonacci sequence: "))
result = calculate_fibonacci_sum(limit)
print(f"The sum of all even Fibonacci numbers up to {limit} is: {result}")
