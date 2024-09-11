
def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        sequence = [0, 1]
        while len(sequence) < n:
            next_num = sequence[-1] + sequence[-2]
            sequence.append(next_num)
        return sequence

# Input number of terms
n = int(input("Enter the number of terms for Fibonacci sequence: "))

# Generate Fibonacci sequence
fib_sequence = fibonacci_sequence(n)

# Print the sequence
print(f"Fibonacci sequence up to {n} terms:")
for num in fib_sequence:
    print(num)
