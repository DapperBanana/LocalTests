
def generate_fibonacci(num_terms):
    fibonacci_seq = []
    a, b = 0, 1
    count = 0

    while count < num_terms:
        fibonacci_seq.append(a)
        a, b = b, a + b
        count += 1

    return fibonacci_seq

num_terms = int(input("Enter the number of terms: "))
fibonacci_seq = generate_fibonacci(num_terms)

print("Fibonacci sequence up to {} terms:".format(num_terms))
print(fibonacci_seq)
