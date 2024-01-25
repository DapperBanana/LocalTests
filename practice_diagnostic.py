
import numpy as np

# Function to check if a matrix is invertible
def is_invertible(matrix):
    # Using numpy's linear algebra function to calculate the determinant
    determinant = np.linalg.det(matrix)
    
    # If the determinant is zero, matrix is not invertible
    if determinant == 0:
        return False
    else:
        return True

# Example usage
matrix = np.array([[2, 1], [1, 3]])
invertible = is_invertible(matrix)

if invertible:
    print("The matrix is invertible")
else:
    print("The matrix is not invertible")
