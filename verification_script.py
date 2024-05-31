
def fibonacci_sum(limit):
    fibonacci = [1, 2]
    even_sum = 2

    while True:
        next_fib = fibonacci[-1] + fibonacci[-2]
        if next_fib > limit:
            break
        fibonacci.append(next_fib)

        if next_fib % 2 == 0:
            even_sum += next_fib

    return even_sum

limit = int(input("Enter the limit for Fibonacci sequence: "))
result = fibonacci_sum(limit)
print(f"The sum of all even Fibonacci numbers up to {limit} is: {result}")
