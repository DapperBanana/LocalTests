
def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        return "Error: Number of columns in matrix A must equal number of rows in matrix B"

    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0]):
            sum = 0
            for k in range(len(B)):
                sum += A[i][k] * B[k][j]
            row.append(sum)
        result.append(row)

    return result

# Example usage
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8),
     [9, 10],
     [11, 12]]

result = matrix_multiply(A, B)
for row in result:
    print(row)
