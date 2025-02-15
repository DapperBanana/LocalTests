
import numpy as np

def is_orthogonal(matrix):
    _, ncols = matrix.shape
    
    if ncols != len(matrix):
        return False

    product = np.dot(matrix, matrix.T)
    identity_matrix = np.eye(ncols)

    return np.allclose(product, identity_matrix)

# Test the function
A = np.array([[1, 0], [0, -1]])
B = np.array([[0, 1], [-1, 0]])
C = np.array([[1, 2], [3, 4]])

print("Matrix A is orthogonal:", is_orthogonal(A))
print("Matrix B is orthogonal:", is_orthogonal(B))
print("Matrix C is orthogonal:", is_orthogonal(C))
