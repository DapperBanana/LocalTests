
def even_fibonacci_sum(limit):
    num1, num2 = 1, 1
    even_sum = 0

    while True:
        new_fib = num1 + num2
        
        if new_fib > limit:
            break
        
        if new_fib % 2 == 0:
            even_sum += new_fib
        
        num1 = num2
        num2 = new_fib

    return even_sum

# Input limit from user
limit = int(input("Enter the limit: "))
result = even_fibonacci_sum(limit)
print(f"The sum of all even Fibonacci numbers up to {limit} is: {result}")
