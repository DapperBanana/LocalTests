
def reverse_matrix(matrix):
    reversed_matrix = []
    for i in range(len(matrix[0])):
        row = [matrix[j][i] for j in range(len(matrix))]
        reversed_matrix.append(row)
    
    return reversed_matrix

# Input matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Reverse the matrix
reversed_matrix = reverse_matrix(matrix)

# Output the reversed matrix
for row in reversed_matrix:
    print(row)
