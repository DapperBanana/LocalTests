
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    min_len = min([len(s) for s in strs])
    longest_prefix = ""
    
    for i in range(min_len):
        current_char = strs[0][i]
        if all(s[i] == current_char for s in strs):
            longest_prefix += current_char
        else:
            break
    
    return longest_prefix

# Test the function
str_list = ["flower", "flow", "flight"]
print(longest_common_prefix(str_list))  # Output: "fl"
