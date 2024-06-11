
def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_num = sequence[i-1] + sequence[i-2]
        if next_num <= n:
            sequence.append(next_num)
        else:
            break
    return sequence

n = int(input("Enter the number of terms for the Fibonacci sequence: "))
fib_seq = fibonacci(n)
print(fib_seq)
