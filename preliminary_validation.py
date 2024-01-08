
import numpy as np

def is_orthogonal(matrix):
    # Check if matrix is square
    if len(matrix) != len(matrix[0]):
        return False
    
    # Convert the matrix to a Numpy array
    matrix = np.array(matrix)
    
    # Calculate the transpose of the matrix
    transpose = np.transpose(matrix)
    
    # Calculate the inverse of the matrix
    try:
        inverse = np.linalg.inv(matrix)
    except np.linalg.LinAlgError:
        return False
    
    # Check if the transpose is equal to the inverse
    return np.allclose(transpose, inverse)

# Test the function
matrix1 = [[1, 0], [0, -1]]
print(is_orthogonal(matrix1))  # True

matrix2 = [[1, 0], [1, 1]]
print(is_orthogonal(matrix2))  # False
