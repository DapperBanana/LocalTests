
def fibonacci(n):
    sequence = []
    if n <= 0:
        return sequence
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = [0, 1]
        for i in range(2, n):
            next_num = sequence[-1] + sequence[-2]
            sequence.append(next_num)
        return sequence

# Get user input for the number of terms
num_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))

# Generate the Fibonacci sequence
fib_sequence = fibonacci(num_terms)

# Print the Fibonacci sequence
print("Fibonacci sequence with {} terms: {}".format(num_terms, fib_sequence))
