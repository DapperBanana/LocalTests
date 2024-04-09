
def determinant(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    if num_rows != num_cols:
        return "Matrix must be square"

    if num_rows == 1:
        return matrix[0][0]

    if num_rows == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    det = 0
    for i in range(num_rows):
        sign = (-1)**i
        sub_matrix = [row[:i] + row[i+1:] for row in matrix[1:]]
        det += sign * matrix[0][i] * determinant(sub_matrix)

    return det

# Test the function
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print("Determinant of the matrix:")
print(determinant(matrix))
