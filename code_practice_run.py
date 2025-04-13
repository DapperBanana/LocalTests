
def longest_common_prefix(strs):
    if not strs:
        return ""

    # Find the shortest string in the list
    min_str = min(strs, key=len)
    
    for i in range(len(min_str)):
        for string in strs:
            if string[i] != min_str[i]:
                return min_str[:i]
    
    return min_str

# Test the function
strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs))  # Output: "fl"

strs = ["dog", "racecar", "car"]
print(longest_common_prefix(strs))  # Output: ""

strs = ["apple", "app", "applause", "ape"]
print(longest_common_prefix(strs))  # Output: "ap"
