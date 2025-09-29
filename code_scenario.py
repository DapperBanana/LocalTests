
def generate_fibonacci(num_terms):
    fibonacci_sequence = [0, 1]
    
    while len(fibonacci_sequence) < num_terms:
        next_num = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_num)
    
    return fibonacci_sequence

num_terms = int(input("Enter the number of terms for Fibonacci sequence: "))
fibonacci_sequence = generate_fibonacci(num_terms)

print("Fibonacci sequence with", num_terms, "terms:")
print(fibonacci_sequence)
