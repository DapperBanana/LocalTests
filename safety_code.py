
def longest_common_prefix(strings):
    if not strings:
        return ""

    prefix = strings[0]
    for s in strings:
        while s[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

# Test the function with some sample strings
strings = ["flower", "flow", "flight"]
print("Longest common prefix:", longest_common_prefix(strings))  # Output: fl
