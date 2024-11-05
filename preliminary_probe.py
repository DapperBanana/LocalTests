
def is_symmetric(matrix):
    n = len(matrix)
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    
    return True

# Test the function
matrix1 = [[1, 2, 3],
           [2, 4, 5],
           [3, 5, 6]]

matrix2 = [[1, 2, 3],
           [2, 4, 5],
           [3, 6, 7]]

print(is_symmetric(matrix1))  # Output: True
print(is_symmetric(matrix2))  # Output: False
