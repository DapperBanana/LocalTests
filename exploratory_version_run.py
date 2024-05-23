
def even_fibonacci_sum(limit):
    f1, f2 = 1, 2
    even_sum = 0
    
    while f2 <= limit:
        if f2 % 2 == 0:
            even_sum += f2
        f1, f2 = f2, f1 + f2
        
    return even_sum

limit = int(input("Enter the limit for Fibonacci numbers: "))
result = even_fibonacci_sum(limit)
print(f"The sum of all even Fibonacci numbers up to {limit} is: {result}")
