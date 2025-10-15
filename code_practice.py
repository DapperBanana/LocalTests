
def fibonacci_sequence(n):
    fibonacci = [0, 1]
    for i in range(2, n):
        next_num = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(next_num)
    return fibonacci

n_terms = int(input("Enter the number of terms: "))
result = fibonacci_sequence(n_terms)
print("Fibonacci sequence up to", n_terms, "terms:")
print(result)
