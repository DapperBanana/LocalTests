
def even_fibonacci_sum(limit):
    fib_list = [1, 2]
    while True:
        next_fib = fib_list[-1] + fib_list[-2]
        if next_fib > limit:
            break
        fib_list.append(next_fib)
    
    even_fib_sum = sum(num for num in fib_list if num % 2 == 0)
    
    return even_fib_sum

limit = int(input("Enter the limit for Fibonacci numbers: "))
result = even_fibonacci_sum(limit)
print(f"The sum of all even Fibonacci numbers up to {limit} is: {result}")
