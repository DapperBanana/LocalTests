
def even_fibonacci_sum(limit):
    fib_list = [1, 2]
    even_sum = 2
    
    while True:
        next_fib = fib_list[-1] + fib_list[-2]
        if next_fib > limit:
            break
        fib_list.append(next_fib)
        if next_fib % 2 == 0:
            even_sum += next_fib
    
    return even_sum

limit = int(input("Enter the limit for Fibonacci numbers: "))
result = even_fibonacci_sum(limit)
print("The sum of all even Fibonacci numbers up to", limit, "is:", result)
