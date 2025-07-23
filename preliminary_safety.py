
def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_number = sequence[i-1] + sequence[i-2]
        if next_number <= n:
            sequence.append(next_number)
        else:
            break
    return sequence

n = int(input("Enter the number of terms: "))
fib_sequence = fibonacci(n)
print("Fibonacci sequence up to", n, "terms:")
print(fib_sequence)
