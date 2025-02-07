
def reverse_matrix(matrix):
    reversed_matrix = []
    for i in range(len(matrix[0])):
        reversed_matrix.append([row[i] for row in matrix])
    return reversed_matrix

# Input matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Reversing the order of rows and columns
reversed_matrix = reverse_matrix(matrix)

# Printing the reversed matrix
for row in reversed_matrix:
    print(row)
