
def even_fibonacci_sum(limit):
    a, b = 1, 2
    total_sum = 0
    while b <= limit:
        if b % 2 == 0:
            total_sum += b
        a, b = b, a + b
    return total_sum

# Test the function with a limit of 400
limit = 400
result = even_fibonacci_sum(limit)
print(f"The sum of all even Fibonacci numbers up to {limit} is: {result}")
