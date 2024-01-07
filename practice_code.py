
import numpy as np

def is_orthogonal(matrix):
    # Convert the matrix to a NumPy array
    matrix = np.array(matrix)

    # Verify the transpose * matrix condition
    transpose_product = np.matmul(np.transpose(matrix), matrix)
    is_identity = np.allclose(transpose_product, np.eye(len(matrix)))

    # Verify the determinant condition
    determinant = np.linalg.det(matrix)
    is_determinant_one = np.isclose(determinant, 1)
    is_determinant_minus_one = np.isclose(determinant, -1)

    return is_identity and (is_determinant_one or is_determinant_minus_one)

# Test the function
matrix1 = [[1, 0], [0, 1]]
print(is_orthogonal(matrix1))  # True

matrix2 = [[1, 1], [-1, 1]]
print(is_orthogonal(matrix2))  # True

matrix3 = [[1, 0], [0, -1]]
print(is_orthogonal(matrix3))  # False
