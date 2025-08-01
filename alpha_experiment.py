
def longest_palindromic_substring(s):
    if s == "":
        return ""
    
    longest = ""
    for i in range(len(s)):
        # Odd length palindromes
        l = i
        r = i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len(longest):
                longest = s[l:r+1]
            l -= 1
            r += 1
        
        # Even length palindromes
        l = i
        r = i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len(longest):
                longest = s[l:r+1]
            l -= 1
            r += 1
    
    return longest

# Input string
s = "babad"
result = longest_palindromic_substring(s)
print("Longest palindromic substring:", result)
