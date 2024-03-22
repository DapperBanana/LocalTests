
def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

n = int(input("Enter the number of terms you want in the Fibonacci sequence: "))
fibonacci_sequence = fibonacci_sequence(n)
print(f"Fibonacci sequence up to {n} terms:")
print(fibonacci_sequence)
