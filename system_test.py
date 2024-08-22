
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    min_str = min(strs, key=len)
    
    for i, char in enumerate(min_str):
        for other_str in strs:
            if other_str[i] != char:
                return min_str[:i]
    
    return min_str

# Test the function
strings = ["flower", "flow", "flight"]
print("Longest common prefix of", strings, "is:", longest_common_prefix(strings))

strings = ["dog", "racecar", "car"]
print("Longest common prefix of", strings, "is:", longest_common_prefix(strings))
