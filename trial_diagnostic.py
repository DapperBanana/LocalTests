
def reverse_matrix(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    reversed_matrix = []
    for i in range(num_cols):
        row = []
        for j in range(num_rows):
            row.append(matrix[j][i])
        reversed_matrix.append(row)

    return reversed_matrix

# Example
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

reversed_matrix = reverse_matrix(matrix)
for row in reversed_matrix:
    print(row)
