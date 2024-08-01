
def fibonacci_sequence(n):
    fib_seq = []
    a, b = 0, 1
    for _ in range(n):
        fib_seq.append(a)
        a, b = b, a + b
    return fib_seq

n = int(input("Enter the number of terms for the Fibonacci sequence: "))
fibonacci_seq = fibonacci_sequence(n)

print("Fibonacci sequence up to", n, "terms:")
print(fibonacci_seq)
