
def longest_common_subsequence(s1, s2):
    m = len(s1)
    n = len(s2)

    # Create a 2D array to store the lengths of the common subsequence
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the longest common subsequence
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs.insert(0, s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(lcs)

# Example usage
s1 = "ABCBDAB"
s2 = "BDCAB"
print("Longest common subsequence:", longest_common_subsequence(s1, s2))  # Output: BCAB
