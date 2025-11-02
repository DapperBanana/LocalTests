
def generate_fibonacci_sequence(num_terms):
    sequence = [0, 1]
    for i in range(2, num_terms):
        next_num = sequence[i-1] + sequence[i-2]
        sequence.append(next_num)
    return sequence

num_terms = int(input("Enter the number of terms: "))

fibonacci_sequence = generate_fibonacci_sequence(num_terms)

print(fibonacci_sequence)
