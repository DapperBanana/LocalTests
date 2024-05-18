
def longest_common_prefix(strings):
    if not strings:
        return ""

    min_str = min(strings, key=len)
    
    for i, char in enumerate(min_str):
        for string in strings:
            if string[i] != char:
                return min_str[:i]
    
    return min_str

# Example
strings = ["flower", "flow", "flight"]
print(longest_common_prefix(strings))  # Output: "fl"
