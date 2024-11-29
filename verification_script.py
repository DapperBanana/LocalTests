
def longest_palindromic_substring(s):
    if len(s) < 1:
        return ""
    
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    
    longest_sub = ""
    for i in range(len(s)):
        # check for odd length palindrome
        sub1 = expand_around_center(i, i)
        if len(sub1) > len(longest_sub):
            longest_sub = sub1
        # check for even length palindrome
        sub2 = expand_around_center(i, i+1)
        if len(sub2) > len(longest_sub):
            longest_sub = sub2
    
    return longest_sub

# Example usage
s = "babad"
print(longest_palindromic_substring(s))  # Output: "aba"
