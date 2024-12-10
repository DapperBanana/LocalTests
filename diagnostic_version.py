
def fibonacci_sequence(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_term = sequence[i-1] + sequence[i-2]
        sequence.append(next_term)
    return sequence

n = int(input("Enter the number of terms in Fibonacci sequence: "))
fibonacci_seq = fibonacci_sequence(n)
print("Fibonacci sequence up to", n, "terms:")
print(fibonacci_seq)
