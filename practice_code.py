
def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

n = int(input("Enter the number of terms in the Fibonacci sequence: "))
fibonacci_sequence = fibonacci_sequence(n)
print(fibonacci_sequence)
