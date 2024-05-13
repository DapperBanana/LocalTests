
def longest_common_prefix(strings):
    if not strings:
        return ""
    
    min_len = min(len(s) for s in strings)
    
    for i in range(min_len):
        if len({s[i] for s in strings}) > 1:
            return strings[0][:i]
    
    return strings[0][:min_len]

# Test the function
strings = ["flower", "flow", "flight"]
print(longest_common_prefix(strings))  # Output: "fl"
