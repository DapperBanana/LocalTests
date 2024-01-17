
def edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a distance matrix
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Fill in the first row and column of the matrix
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Populate the rest of the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],        # Insertion
                                   dp[i - 1][j],        # Deletion
                                   dp[i - 1][j - 1])    # Substitution

    # Return the edit distance between the two strings
    return dp[m][n]


# Test the function
str1 = "kitten"
str2 = "sitting"
print("Edit distance between '{}' and '{}' is {}".format(str1, str2, edit_distance(str1, str2)))

