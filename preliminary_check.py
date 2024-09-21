
def minor(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]

def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    else:
        det = 0
        for j in range(len(matrix)):
            det += ((-1) ** j) * matrix[0][j] * determinant(minor(matrix, 0, j))
        return det

# Test the program with a sample matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matrix:")
for row in matrix:
    print(row)
print("Determinant:", determinant(matrix))
