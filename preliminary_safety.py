
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    min_str = min(strs, key=len)
    
    for i, char in enumerate(min_str):
        for string in strs:
            if string[i] != char:
                return min_str[:i]
    
    return min_str

# Test the function
strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs))  # Output: "fl"

strs = ["dog", "racecar", "car"]
print(longest_common_prefix(strs))  # Output: ""
