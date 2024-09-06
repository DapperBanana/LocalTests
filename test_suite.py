
def fibonacci_sum(limit):
    fib_seq = [1, 1]
    even_sum = 0

    while True:
        next_fib = fib_seq[-1] + fib_seq[-2]
        if next_fib > limit:
            break
        fib_seq.append(next_fib)

    for num in fib_seq:
        if num % 2 == 0:
            even_sum += num

    return even_sum

limit = int(input("Enter a limit: "))
result = fibonacci_sum(limit)
print(f"The sum of all even Fibonacci numbers up to {limit} is: {result}")
