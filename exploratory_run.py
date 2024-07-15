
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

n = int(input("Enter the number of terms for Fibonacci sequence: "))
fib_series = fibonacci(n)
print("Fibonacci sequence with", n, "terms:")
print(fib_series)
