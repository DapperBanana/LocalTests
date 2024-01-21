
def fibonacci_sequence(num_terms):
    sequence = []
    a, b = 0, 1
    for _ in range(num_terms):
        sequence.append(a)
        a, b = b, a + b
    return sequence

num_terms = int(input("Enter the number of terms: "))
fib_sequence = fibonacci_sequence(num_terms)
print("Fibonacci Sequence:", fib_sequence)
