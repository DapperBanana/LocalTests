
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    min_str = min(strs, key=len)
    
    for i in range(len(min_str)):
        for string in strs:
            if string[i] != min_str[i]:
                return min_str[:i]
    
    return min_str

# Test the function
strs = ["leetcode", "leet", "lee", "le"]
print(longest_common_prefix(strs))  # Output: "le"
