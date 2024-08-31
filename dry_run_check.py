
def fibonacci_sequence(n):
    sequence = [0, 1]
    
    if n <= 0:
        return "Please enter a positive integer."
    
    elif n == 1:
        return [0]
    
    elif n == 2:
        return sequence
    
    else:
        for i in range(2, n):
            next_term = sequence[-1] + sequence[-2]
            sequence.append(next_term)
            
        return sequence

n = int(input("Enter the number of terms for the Fibonacci sequence: "))
print(fibonacci_sequence(n))
