
import numpy as np

def is_orthogonal(matrix):
    transpose = np.transpose(matrix)
    product = np.dot(matrix, transpose)

    identity = np.identity(len(matrix))

    if np.allclose(product, identity):
        return True
    else:
        return False

# Example matrix
matrix = np.array([[1, 0],
                   [0, -1]])

if is_orthogonal(matrix):
    print("The given matrix is orthogonal.")
else:
    print("The given matrix is not orthogonal.")
