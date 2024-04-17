
def is_symmetric(matrix):
    # Check if the matrix is square
    if len(matrix) != len(matrix[0]):
        return False
    
    # Check if the transpose of the matrix is equal to the original matrix
    transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0])]
    
    return matrix == transposed_matrix

# Test the function
matrix1 = [[1, 2, 3],
           [2, 4, 5],
           [3, 5, 6]]

matrix2 = [[1, 2, 3],
           [2, 4, 5],
           [3, 6, 7]]

print(is_symmetric(matrix1))  # Output: True
print(is_symmetric(matrix2))  # Output: False
