
def longest_common_prefix(strs):
    if not strs:
        return ""

    min_str = min(strs)
    max_str = max(strs)

    for i, c in enumerate(min_str):
        if c != max_str[i]:
            return min_str[:i]

    return min_str

# Test the function
strs = ['flower', 'flow', 'flight']
print(longest_common_prefix(strs))  # Output: 'fl'
