
def reverse_matrix(matrix):
    reversed_matrix = []
    for i in range(len(matrix[0])):
        reversed_matrix.append([row[i] for row in matrix])
    return reversed_matrix

# Example matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

reversed_matrix = reverse_matrix(matrix)

for row in reversed_matrix:
    print(row)
