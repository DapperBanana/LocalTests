
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    min_str = min(strs, key=len)
    
    for i, char in enumerate(min_str):
        for s in strs:
            if s[i] != char:
                return min_str[:i]
    
    return min_str

# Test the function
strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs))  # Output: "fl"
