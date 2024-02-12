
def find_longest_common_subsequence(string1, string2):
    m = len(string1)
    n = len(string2)

    # Create a table to store the lengths of longest common subsequence
    # where dp[i][j] represents the length of longest common subsequence
    # of string1[:i] and string2[:j].
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Calculate dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Construct the longest common subsequence
    longest_common_subsequence = ""
    i, j = m, n
    while i > 0 and j > 0:
        if string1[i - 1] == string2[j - 1]:
            longest_common_subsequence = string1[i - 1] + longest_common_subsequence
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return longest_common_subsequence


# Test the program
string1 = "ABCDGH"
string2 = "AEDFHR"
print("Longest common subsequence:", find_longest_common_subsequence(string1, string2))

string1 = "AGGTAB"
string2 = "GXTXAYB"
print("Longest common subsequence:", find_longest_common_subsequence(string1, string2))
