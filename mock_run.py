
import numpy as np

def is_invertible(matrix):
    try:
        np.linalg.inv(matrix)
        return True
    except np.linalg.LinAlgError:
        return False

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

if matrix.shape[0] == matrix.shape[1]:
    if is_invertible(matrix):
        print("The matrix is invertible.")
    else:
        print("The matrix is not invertible.")
else:
    print("The matrix is not square.")
