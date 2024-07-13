
def longest_common_subsequence(str1, str2):
    m = len(str1)
    n = len(str2)

    # Creating a 2D list to store the length of longest common subsequence
    dp = [[0]*(n+1) for _ in range(m+1)]

    # Fill the dp array with length of longest common subsequence
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Backtrack to find the actual longest common subsequence
    i, j = m, n
    lcs = ""
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs = str1[i-1] + lcs
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return lcs

# Test the function with example input
str1 = "ABCDGH"
str2 = "AEDFHR"
print("Longest common subsequence:", longest_common_subsequence(str1, str2))
