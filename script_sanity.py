
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    for string in strs[1:]:
        while string.find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

# Test the function
strs = ["flower", "flow", "flight"]
print("Longest common prefix:", longest_common_prefix(strs))
