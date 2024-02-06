
def fibonacci_sequence(num_terms):
    # Initialize the first two terms of the sequence
    sequence = [0, 1]
    
    # Generate the subsequent terms of the sequence
    for i in range(2, num_terms):
        next_term = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_term)
    
    return sequence

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms to generate: "))

# Generate and print the Fibonacci
fibonacci = fibonacci_sequence(num_terms)
print("Fibonacci sequence:")
print(fibonacci)
