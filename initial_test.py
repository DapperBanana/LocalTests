
def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    
    det = 0
    for i in range(len(matrix)):
        sign = (-1) ** i
        sub_matrix = [row[:i] + row[i+1:] for row in matrix[1:]]
        det += sign * matrix[0][i] * determinant(sub_matrix)
        
    return det

# Test the program
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print("Matrix:")
for row in matrix:
    print(row)

print("Determinant:", determinant(matrix))
