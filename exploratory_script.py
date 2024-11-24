
def is_magic_square(matrix):
    n = len(matrix)
    
    # Calculate the sum of the first row
    sums = [sum(matrix[0])]
    
    # Calculate the sum of rows, columns, and diagonals
    for i in range(1, n):
        sums.append(sum(matrix[i]))
        sums.append(sum(row[i] for row in matrix))
    sums.append(sum(matrix[i][i] for i in range(n)))
    sums.append(sum(matrix[i][n-1-i] for i in range(n)))
    
    # Check if all sums are equal
    return len(set(sums)) == 1

# Example matrix
matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

if is_magic_square(matrix):
    print("The matrix is a magic square")
else:
    print("The matrix is not a magic square")
