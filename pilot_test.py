
def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    
    det = 0
    for i in range(n):
        minor = [[matrix[j][k] for k in range(n) if k != i] for j in range(1, n)]
        det += ((-1) ** i) * matrix[0][i] * determinant(minor)
    
    return det

# Test the program
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
  
print("Matrix:")
for row in matrix:
    print(row)

print("\nDeterminant:", determinant(matrix))
