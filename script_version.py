
def longest_common_prefix(strs):
    if not strs:
        return ""

    shortest_str = min(strs, key=len)
    
    for i, char in enumerate(shortest_str):
        for other_str in strs:
            if other_str[i] != char:
                return shortest_str[:i]
    
    return shortest_str

# Test the longest_common_prefix function
result = longest_common_prefix(["flower", "flow", "flight"])
print(result)  # Output: "fl"
