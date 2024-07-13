
def fibonacci(n):
    fibonacci_seq = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_seq.append(a)
        a, b = b, a + b
    return fibonacci_seq

# Input number of terms
num_terms = int(input("Enter number of terms: "))

if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    fibonacci_seq = fibonacci(num_terms)
    print("Fibonacci sequence up to", num_terms, "terms:")
    print(fibonacci_seq)
