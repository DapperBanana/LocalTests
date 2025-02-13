
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    for i in range(len(strs[0])):
        for string in strs[1:]:
            if i >= len(string) or string[i] != strs[0][i]:
                return strs[0][:i]
    
    return strs[0]

# Test the function
str_list = ["flower", "flight", "flow"]
print(longest_common_prefix(str_list))  # Output: "fl"
