
def is_symmetric(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Check if the matrix is square
    if rows != cols:
        return False
    
    # Check if the matrix is symmetric
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

# Test the function
matrix1 = [[1, 2, 3],
          [2, 4, 5],
          [3, 5, 6]]

matrix2 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(is_symmetric(matrix1)) # Output: True
print(is_symmetric(matrix2)) # Output: False
