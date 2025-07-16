
def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = strs[0]
    for string in strs[1:]:
        i = 0
        while i < len(prefix) and i < len(string) and prefix[i] == string[i]:
            i += 1
        prefix = prefix[:i]

    return prefix

# Test the function
str_list = ["flower", "flow", "flight"]
print(longest_common_prefix(str_list))  # Output: "fl"
