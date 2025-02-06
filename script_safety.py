
def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence

n = int(input("Enter the number of terms in the Fibonacci sequence: "))
result = fibonacci_sequence(n)
print(result)
