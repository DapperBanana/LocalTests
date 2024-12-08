
import numpy as np

def is_orthogonal(matrix):
    # Calculate the inverse of the matrix
    inv_matrix = np.linalg.inv(matrix)
    
    # Calculate the transpose of the matrix
    transpose_matrix = np.transpose(matrix)
    
    # Check if the inverse is equal to the transpose
    if np.allclose(inv_matrix, transpose_matrix):
        return True
    else:
        return False

# Test the function with an example matrix
matrix = np.array([[1, 0],
                   [0, -1]])

if is_orthogonal(matrix):
    print("The matrix is orthogonal.")
else:
    print("The matrix is not orthogonal.")
