
def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

n = int(input("Enter the number of terms for the Fibonacci sequence: "))
fibonacci = fibonacci_sequence(n)
print("Fibonacci sequence up to", n, "terms:", fibonacci)
