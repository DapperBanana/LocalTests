
def longest_common_subsequence(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a 2D list to store the length of common subsequence at each index
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the 2D list based on the characters of the two strings
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Retrieve the longest common subsequence
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs.insert(0, str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(lcs)

# Test the function
str1 = "ABCBDAB"
str2 = "BDCAB"
print("Longest common subsequence:", longest_common_subsequence(str1, str2))
