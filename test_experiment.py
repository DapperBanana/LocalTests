
def longest_palindromic_substring(s):
    if len(s) == 0:
        return ""
    
    start = 0
    end = 0
    for i in range(len(s)):
        len1 = expand_around_center(s, i, i) # for odd length
        len2 = expand_around_center(s, i, i+1) #for even length
        length = max(len1, len2)
        
        if length > end - start:
            start = i - (length - 1) // 2
            end = i + length // 2
    
    return s[start:end+1]

def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

# Test the function with an example string
s = "babad"
print(longest_palindromic_substring(s))
