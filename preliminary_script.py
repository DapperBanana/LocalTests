
def determinant(matrix):
    size = len(matrix)
    
    if size == 1:
        return matrix[0][0]
    
    det = 0
    sign = 1
    
    for i in range(size):
        sub_matrix = [[matrix[j][k] for k in range(size) if k != i] for j in range(1, size)]
        det += sign * matrix[0][i] * determinant(sub_matrix)
        sign *= -1

    return det

# Test the program
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)

print("\nDeterminant:", determinant(matrix))
