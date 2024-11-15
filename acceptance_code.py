
def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]

def longest_palindromic_substring(s):
    if len(s) == 0:
        return ""

    longest = ""
    for i in range(len(s)):
        # For odd length palindromes
        palindrome1 = expand_around_center(s, i, i)
        if len(palindrome1) > len(longest):
            longest = palindrome1

        # For even length palindromes
        palindrome2 = expand_around_center(s, i, i + 1)
        if len(palindrome2) > len(longest):
            longest = palindrome2

    return longest

# Test the function
s = "babad"
print(longest_palindromic_substring(s))  # Output: "bab" or "aba"

s = "cbbd"
print(longest_palindromic_substring(s))  # Output: "bb"
