
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for i in range(n):
        fib_sequence.append(a)
        a, b = b, a+b
    return fib_sequence

n_terms = int(input("Enter the number of terms for Fibonacci sequence: "))
fib_sequence = fibonacci(n_terms)
print("Fibonacci sequence up to", n_terms, "terms:")
print(fib_sequence)
