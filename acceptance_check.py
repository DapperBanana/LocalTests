
def matrix_multiply(A, B):
    # check if dimensions are compatible for matrix multiplication
    if len(A[0]) != len(B):
        print("Error: Incompatible dimensions for matrix multiplication.")
        return
    
    # create matrix for resulting product
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    
    # perform matrix multiplication
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

# test the matrix multiplication function
A = [[1, 2, 3],
     [4, 5, 6]]
B = [[7, 8],
     [9, 10],
     [11, 12]]

result = matrix_multiply(A, B)

if result:
    for row in result:
        print(row)
