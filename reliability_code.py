
def fibonacci(n):
    fib_seq = [0, 1]
    
    while len(fib_seq) < n:
        next_num = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_num)
    
    return fib_seq

n_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))
fib_sequence = fibonacci(n_terms)

print(f"Fibonacci sequence up to {n_terms} terms:")
print(fib_sequence)
