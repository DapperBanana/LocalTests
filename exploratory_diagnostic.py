
import numpy as np

def determinant(matrix):
    return np.linalg.det(matrix)

# Input a square matrix
n = int(input("Enter the size of the square matrix: "))
matrix = []
print("Enter the elements of the square matrix:")
for _ in range(n):
    row = list(map(float, input().split()))
    matrix.append(row)

# Calculate the determinant of the matrix
det = determinant(matrix)

# Output the determinant
print("Determinant of the matrix:")
print(det)
