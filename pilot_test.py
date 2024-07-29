
def even_fibonacci_sum(limit):
    fib_list = [1, 2]
    sum = 2
    while True:
        next_fib = fib_list[-1] + fib_list[-2]
        if next_fib > limit:
            break
        fib_list.append(next_fib)
        if next_fib % 2 == 0:
            sum += next_fib
    return sum

limit = int(input("Enter the limit: "))
result = even_fibonacci_sum(limit)
print("The sum of all even Fibonacci numbers up to", limit, "is:", result)
