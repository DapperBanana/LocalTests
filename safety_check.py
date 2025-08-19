
def generate_fibonacci_sequence(n):
    fibonacci_sequence = [0, 1]
    
    while len(fibonacci_sequence) < n:
        next_num = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_num)
    
    return fibonacci_sequence

n = int(input("Enter the number of terms for the Fibonacci sequence: "))

if n <= 0:
    print("Number of terms should be a positive integer.")
else:
    fibonacci_sequence = generate_fibonacci_sequence(n)
    print(f"Fibonacci sequence up to {n} terms: {fibonacci_sequence}")
