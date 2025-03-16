
def lcs(X, Y):
    m = len(X)
    n = len(Y)
    
    # Create a 2D array to store the length of longest common subsequence at each position
    L = [[0] * (n + 1) for i in range(m + 1)]
    
    # Building the L array in a bottom-up manner
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    
    # The length of the longest common subsequence will be at the bottom-right corner of L
    index = L[m][n]
    lcs = [""] * (index + 1)
    lcs[index] = ""
    
    # Backtracking to find the longest common subsequence
    i = m
    j = n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(lcs)

# Test the function with two strings
X = "ABCBDAB"
Y = "BDCAB"
print("Longest common subsequence of", X, "and", Y, "is:", lcs(X, Y))
