
def expand_from_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right]

def longest_palindromic_substring(s):
    if len(s) == 0:
        return ""

    longest_palindrome = ""
    for i in range(len(s)):
        # Expand around center for odd length palindromes
        palindrome1 = expand_from_center(s, i, i)
        # Expand around center for even length palindromes
        palindrome2 = expand_from_center(s, i, i+1)

        curr_longest = palindrome1 if len(palindrome1) > len(palindrome2) else palindrome2
        if len(curr_longest) > len(longest_palindrome):
            longest_palindrome = curr_longest

    return longest_palindrome

# Test the function with an example
s = "babad"
print("Longest palindromic substring:", longest_palindromic_substring(s))
