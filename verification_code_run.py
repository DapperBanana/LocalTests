
def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right]

def longest_palindromic_substring(s):
    if len(s) < 1:
        return ""

    longest_palindrome = s[0]
    for i in range(0, len(s)):
        odd_palindrome = expand_around_center(s, i, i)
        even_palindrome = expand_around_center(s, i, i+1)

        if len(odd_palindrome) > len(longest_palindrome):
            longest_palindrome = odd_palindrome

        if len(even_palindrome) > len(longest_palindrome):
            longest_palindrome = even_palindrome

    return longest_palindrome

# Test the function
s = "babad"
print(longest_palindromic_substring(s))  # Output: "bab" or "aba"

s = "cbbd"
print(longest_palindromic_substring(s))  # Output: "bb"
