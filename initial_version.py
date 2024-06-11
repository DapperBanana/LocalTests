
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    # Find the minimum length string from the list
    min_length = min([len(s) for s in strs])
    
    prefix = ""
    
    for i in range(min_length):
        char = strs[0][i]
        if all(s[i] == char for s in strs):
            prefix += char
        else:
            break
    
    return prefix

# Test the function
strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs))  # Output: "fl"

strs = ["dog", "racecar", "car"]
print(longest_common_prefix(strs))  # Output: ""
