
def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    
    det = 0
    for i in range(n):
        sign = (-1) ** i
        minor = [row[:i] + row[i+1:] for row in matrix[1:]]
        det += sign * matrix[0][i] * determinant(minor)
    
    return det

# Test the function
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Input Matrix:")
for row in matrix:
    print(row)

print("\nDeterminant:", determinant(matrix))
