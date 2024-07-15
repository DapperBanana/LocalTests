
def reverse_matrix(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        new_row = []
        for row in matrix:
            new_row.append(row[i])
        new_matrix.append(new_row)
    return new_matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

# Sample input matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print("Original matrix:")
print_matrix(matrix)

reversed_matrix = reverse_matrix(matrix)

print("\nReversed matrix:")
print_matrix(reversed_matrix)
