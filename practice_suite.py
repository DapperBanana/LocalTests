
def fibonacci_sequence(n):
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        next_num = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_num)
    return fib_seq

n_terms = int(input("Enter the number of terms for Fibonacci sequence: "))
fibonacci_seq = fibonacci_sequence(n_terms)

print("Fibonacci sequence up to {} terms:".format(n_terms))
for num in fibonacci_seq:
    print(num)
