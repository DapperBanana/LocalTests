
def generate_fibonacci_sequence(num_terms):
    fibonacci_sequence = []
    a, b = 0, 1
    for _ in range(num_terms):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence

num_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))
fibonacci_sequence = generate_fibonacci_sequence(num_terms)

print("Fibonacci sequence up to", num_terms, "terms:")
print(fibonacci_sequence)
