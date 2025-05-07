
def longest_common_prefix(strs):
    if not strs:
        return ""

    min_str = min(strs, key=len)

    for i, char in enumerate(min_str):
        for other_str in strs:
            if other_str[i] != char:
                return min_str[:i]

    return min_str

# Example
str_list = ["flower", "flow", "flight"]
print(longest_common_prefix(str_list))  # Output: "fl"
