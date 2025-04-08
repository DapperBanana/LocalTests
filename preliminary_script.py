
def generate_fibonacci_sequence(n):
    fibonacci_sequence = [0, 1]
    
    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    
    return fibonacci_sequence

n = int(input("Enter the number of terms in Fibonacci sequence: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    fibonacci_sequence = generate_fibonacci_sequence(n)
    print("Fibonacci sequence:")
    print(fibonacci_sequence)
