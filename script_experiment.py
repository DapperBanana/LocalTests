
def reverse_matrix(matrix):
    reversed_matrix = []
    for i in range(len(matrix[0])):
        reversed_row = []
        for row in matrix:
            reversed_row.append(row[i])
        reversed_matrix.append(reversed_row)
    return reversed_matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

# Example input matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

reversed_matrix = reverse_matrix(matrix)

print("Original Matrix:")
print_matrix(matrix)

print("\nReversed Matrix:")
print_matrix(reversed_matrix)
